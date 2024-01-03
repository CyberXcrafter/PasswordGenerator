import random
import string

def generate_password(length=12):
    # Define characters to be used in the password (you can customize this)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a password of default length (12 characters)
generated_password = generate_password()
print("Generated Password:", generated_password)
