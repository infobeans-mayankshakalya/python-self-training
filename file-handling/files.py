action=input("Enter 'r' to read a file or 'w' to write to a file: ").strip().lower()
if action not in ['r', 'w']:
    print("Invalid action. Please enter 'r' or 'w'.")
    exit()
match(action):
    case 'r':
        file_name = 'myfile.txt'
        try:
            with open(file_name, 'r') as file:
                content = file.read()
            print(f"Content of {file_name}:\n{content}")
        except FileNotFoundError:
            print(f"The file {file_name} does not exist.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
    case 'w':
        content = input("Enter the content of the file: ").strip()
        content = f"{content}\n"
        if not content:
            print("No content provided. Exiting.")
        else:
            file_name = 'myfile.txt'
            try:
                with open(file_name, 'a') as file:
                    file.write(content)
                print(f"Content written to {file_name} successfully.")
            except Exception as e:
                print(f"An error occurred while writing to the file: {e}")