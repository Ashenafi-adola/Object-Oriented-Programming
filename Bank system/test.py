import getpass

def main():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # In a real application, you would now use 'username' and 'password'
    # to authenticate the user or perform other secure operations.
    print(f"Username: {username}")
    print(f"Password (hidden): {'*' * len(password)}") # Display masked length for demonstration

if __name__ == "__main__":
    main()