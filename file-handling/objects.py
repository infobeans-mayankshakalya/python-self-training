import cache

class Objects:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

def main():
    cacheObj = cache.CacheManager()
    obj1_cached = cacheObj.get_cache('obj1')
    obj2_cached = cacheObj.get_cache('obj2')
    if obj1_cached:
        print("Cached Object 1:")
        obj1_cached.display()
    else:
        obj1 = Objects("Alice", 30)
        cacheObj.set_cache('obj1', obj1)
        obj1.display()

    if obj2_cached:
        print("Cached Object 2:")
        obj2_cached.display()
    else:
        obj2 = Objects("Bob", 25)
        cacheObj.set_cache('obj2', obj2)
        obj2.display()
main()