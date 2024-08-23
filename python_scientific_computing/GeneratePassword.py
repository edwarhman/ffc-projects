import re
import secrets
import string


def generate_password(
    length=16,
    nums=1,
    special_chars=1,
    uppercase=1,
    lowercase=1
):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        if is_valid_password(
            password,
            nums,
            special_chars,
            uppercase,
            lowercase
        ):
            break

    return password


def is_valid_password(
    password,
    symbols=string.punctuation,
    nums=1,
    special_chars=1,
    uppercase=1,
    lowercase=1
):
    # Define the possible characters for the password
    constraints = [
        (nums, r'\d'),
        (special_chars, fr'[{symbols}]'),
        (uppercase, r'[A-Z]'),
        (lowercase, r'[a-z]')
    ]

    # Check constraints
    return all(
        constraint <= len(re.findall(pattern, password))
        for constraint, pattern in constraints
    )


if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
