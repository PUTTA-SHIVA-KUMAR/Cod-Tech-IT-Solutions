import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    if complexity == 'low':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation + '£$%^&*()@!'
    else:
        print("Error: Invalid complexity level")
        return
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length and complexity
length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity level (low, medium, high): ")

# Generate and print password
password = generate_password(length, complexity)
print("Generated Password:", password)
