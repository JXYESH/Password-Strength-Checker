#  Password Strength Checker

A Python program that evaluates the strength of a password. The program should check for factors such as length, use of uppercase and lowercase letters, numbers, and special characters. Based on these checks, classify the password and provide clear feedback to improve security.

##  Features

-  Hidden password input for security
-  Checks password length (minimum 8 characters)
-  Checks for uppercase and lowercase letters
-  Checks for numbers (digits)
-  Checks for special characters (!@#$%^&* etc.)
-  Classifies passwords as Weak, Moderate, or Strong
-  Provides specific suggestions to improve password strength

##  Sample Output

### Test 1: Weak Password
Input: `jb123`
Enter your password (what you type in will be hidden for security):

Password Strength: Weak
Suggestions to improve your password:

Use atleast 8 characters.

Add atleast one uppercase letter.

Add atleast one special character.

### Test 2: Moderate Password
Input: `jayesh56`
Enter your password (what you type in will be hidden for security):

Password Strength: Moderate
Suggestions to improve your password:

Add atleast one uppercase letter.

Add atleast one special character.

### Test 3: Strong Password
Input: `Jayesh@2026#`
Enter your password (what you type in will be hidden for security):

Password Strength: Strong
Feedback: Great password! Your password meets all security criteria.

