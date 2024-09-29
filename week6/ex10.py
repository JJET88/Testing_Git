def validate_password(password):
    # Initialize flags
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    # Check if the password meets the length requirement
    if len(password) < 6 or len(password) > 16:
        return False

    # Iterate through each character of the password
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True

    # Validate based on flags
    if has_lower and has_upper and has_digit and has_special:
        return True
    else:
        return False

# Accept input from the user
password = input("Enter your password: ")

# Validate the password
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
