

import string
from getpass import getpass

password = getpass("Enter your password (what you type in will be hidden for security): ")
score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Use atleast 8 characters.")

if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add atleast one uppercase letter.")

if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Add atleast one lowercase letter.")

if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add atleast one number.")

if any(char in string.punctuation for char in password):
    score += 1
else:
    feedback.append("Add atleast one special character.")

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Strength:", strength)

if strength != "Strong":
    print("Suggestions to improve your password:")
    for item in feedback:
        print("-", item)
else:
    print("Your password is secure")