import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (!@#$, etc).")

    # Strength feedback
    if strength == 5:
        return "Strong password ✅"
    elif strength >= 3:
        return "Moderate password ⚠️\n" + "\n".join(feedback)
    else:
        return "Weak password ❌\n" + "\n".join(feedback)


# Example usage
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print(check_password_strength(pwd))
