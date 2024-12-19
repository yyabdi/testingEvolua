# Vulnerable and Erroneous Python Script

import os
import hashlib

#testing add a commit to pre committed code

# Cybersecurity Error 1: Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"

def login(user, pwd):
    # Logic Error: Using '==' instead of a secure comparison
    if user == USERNAME and pwd == PASSWORD:
        print("Login successful!")
    else:
        print("Invalid credentials.")

# Cybersecurity Error 2: Weak password hashing
def store_password(plain_password):
    # Logic Error: Using MD5, which is insecure
    hashed_password = hashlib.md5(plain_password.encode()).hexdigest()
    print(f"Storing password hash: {hashed_password}")

# Cybersecurity Error 3: Command injection vulnerability
def delete_file(filename):
    os.system(f"rm -rf {filename}")  # Unsafe way to handle file deletions

# Logical Error: Misplaced return statement
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        print("Invalid dimensions!")
        return  # Should return a value (e.g., 0 or raise an exception)
    return length * width

# Logical Error: Infinite loop with no termination condition
def process_items(items):
    i = 0
    while i < len(items):
        print(f"Processing item: {items[i]}")

# Main program execution
if __name__ == "__main__":
    print("Welcome to the vulnerable application!")

    # Cybersecurity Error 4: Lack of input validation
    user_input = input("Enter filename to delete: ")
    delete_file(user_input)  # Command injection risk

    # Example of insecure password storage
    store_password("user_password")

    # Logical errors in function usage
    print("Area calculation example:")
    result = calculate_area(5, -10)  # Incorrect dimensions, logical error
    print(f"Calculated area: {result}")

    print("Processing items:")
    process_items(["item1", "item2", "item3"])  # Infinite loop
