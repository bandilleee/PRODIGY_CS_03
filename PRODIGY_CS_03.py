import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Upper and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append('Include both uppercase and lowercase letters.')

    # Number check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (e.g., @, #, !).")

    # Determine password strength
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_message = strength_levels[strength]

    # Output result
    print(f"\nPassword Strength: {strength_message}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f"- {f}")

# Get user input
user_password = input("Enter your password: ")
check_password_strength(user_password)
