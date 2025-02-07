import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    # Define character sets
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits if use_digits else ""  # 0-9
    special = string.punctuation if use_special else ""  # Special characters

    # Combine character sets
    all_chars = lower + upper + digits + special
    
    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits) if use_digits else "",
        random.choice(special) if use_special else "",
    ]

    # Fill the rest of the password length randomly
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle to remove predictable patterns
    random.shuffle(password)
    
    return "".join(password)

# User input for password length
length = int(input("Enter password length: "))
use_digits = input("Include numbers? (yes/no): ").strip().lower() == "yes"
use_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

# Generate and display password
password = generate_password(length, use_digits, use_special)
print("Generated Password:", password)
