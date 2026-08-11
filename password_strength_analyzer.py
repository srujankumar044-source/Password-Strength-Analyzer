import re
import secrets
import string
from getpass import getpass


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "abc123",
}


def check_password(password):
    """Return score, strength, and improvement suggestions."""
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"""[!@#$%^&*(),.?":{}|<>_\-+=/\\\[\]]""", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid common passwords.")

    if re.search(r"(.)\1\1", password):
        score = max(0, score - 1)
        suggestions.append("Avoid repeating the same character many times.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    elif score == 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, suggestions


def generate_password(length=14):
    """Generate a random password using Python's secrets module."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    password = getpass("Enter your password: ")
    score, strength, suggestions = check_password(password)

    print("\nPassword Analysis")
    print("-" * 25)
    print("Score    :", score, "/ 6")
    print("Strength :", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nYour password satisfies all basic checks.")

    if strength in {"Weak", "Medium"}:
        print("\nSuggested stronger password:")
        print(generate_password())

    print("\nNote: Your entered password is not displayed or stored.")


if __name__ == "__main__":
    main()
