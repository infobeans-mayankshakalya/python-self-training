import pickle, json, os

class CacheManager:

    _registry = {}
    _cache_fragement = ''

    def __init__(self):
        infra_status = self._create_infra()
        if infra_status:
            print('Initial setup done.')
        self._registry = self._get_registry()

    def get_cache(self, key):
        if key in self._registry:
            try:
                f = open( f"{self.get_fmt_path()}/"+self._registry[key], 'rb')
                value = pickle.load(f)
                f.close()
                return value
            except (FileNotFoundError, EOFError):
                print("Cache file not found or is empty. Returning None.")
                return None

    def set_cache(self, key, value):
        try:
            self._cache_fragement = f"{hash(value)}.fmt"
            f = open( f"{self.get_fmt_path()}/"+self._cache_fragement, 'wb+')
            pickle.dump(value,f)
            self.update_registry(key, self._cache_fragement)
            f.close()
        except (FileNotFoundError, EOFError):
            print("Cache file not found or is empty. Creating a new cache file.")

    def update_registry(self, key = None, value = None):
        if key is not None and value is not None:    
            r=open(f"{self.get_fmt_path()}/"+'registry.json', 'r+')
            self._registry = json.loads(r.read())
            self._registry[key] = value
            r.truncate(0)  # Clear the file before writing
            r.seek(0)  # Move the cursor to the beginning of the file
            json.dump(self._registry, r, indent=4)
            r.close()


    def _get_registry(self):
        r=open(f"{self.get_fmt_path()}/"+'registry.json', 'r+')
        registry = json.loads(r.read())
        r.close()
        return registry
    
    def _create_infra(self):
        new_dir = self.get_fmt_path()
        # Create the directory if it doesn't exist
        os.makedirs(new_dir, exist_ok=True)
        try:
            with open( new_dir+"/registry.json", 'x') as f:
                f.write("{}")  # optional initial content
        except FileExistsError:
            return False
        return True

    def get_fmt_path(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the path for the new directory
        return os.path.join(script_dir, '.cache_fragments')

