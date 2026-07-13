"""
Password Generator & Strength Checker
Author: Prachi
"""

import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a random password based on chosen options."""
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if length < 4:
        print("Password length should be at least 4 for decent security.")
        length = 4

    password = "".join(random.choice(chars) for _ in range(length))
    return password


def check_strength(password):
    """Check password strength and return a rating."""
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("==== PASSWORD GENERATOR ====\n")

    while True:
        print("1. Generate a new password")
        print("2. Check strength of my own password")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            try:
                length = int(input("Password length (default 12): ") or 12)
            except ValueError:
                length = 12

            use_upper = input("Include uppercase letters? (y/n): ").lower() != "n"
            use_digits = input("Include numbers? (y/n): ").lower() != "n"
            use_symbols = input("Include symbols? (y/n): ").lower() != "n"

            password = generate_password(length, use_upper, use_digits, use_symbols)
            strength = check_strength(password)

            print(f"\nGenerated Password: {password}")
            print(f"Strength: {strength}\n")

        elif choice == "2":
            password = input("Enter a password to check: ")
            strength = check_strength(password)
            print(f"Strength: {strength}\n")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
