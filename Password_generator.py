import random
import string

# Function to generate password
def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main function
def main():
    # Prompt user to input desired password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
        else:
            password = generate_password(length)
            print("Generated Password: ", password)
    except ValueError:
        print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
