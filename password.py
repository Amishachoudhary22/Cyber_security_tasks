import re

def assess_password_strength(password):
    # Initialize strength score
    strength_score = 0
    feedback = []

    # Check the length of the password
    if len(password) >= 12:
        strength_score += 3
    elif len(password) >= 8:
        strength_score += 2
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 2
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 2
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength_score += 2
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        strength_score += 2
    else:
        feedback.append("Password should include at least one special character.")

    # Determine strength level based on score
    if strength_score <= 3:
        strength_level = "Weak"
    elif strength_score <= 6:
        strength_level = "Moderate"
    else:
        strength_level = "Strong"

    # Compile feedback
    feedback_message = "Password Strength: " + strength_level
    if feedback:
        feedback_message += "\nSuggestions:\n" + "\n".join(feedback)

    return feedback_message

# Main function to get user input and assess password strength
def main():
    password = input("Enter your password: ")
    print(assess_password_strength(password))

if __name__ == "__main__":
    main()
