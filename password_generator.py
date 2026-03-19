import random
import string

# Combine all character sets
characters = string.ascii_letters + string.digits + string.punctuation

# Ask user for password length
length = int(input("Enter password length: "))

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Output
print("Generated Password:", password)
