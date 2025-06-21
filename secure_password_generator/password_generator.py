import string
import secrets


def generate_password(min_length: int, max_length: int, use_numbers: bool = True,
                      use_special_chars: bool = True, required_types: bool = True) -> str:
    if min_length > max_length:
        raise ValueError("Minimum length cannot be greater than maximum length.")

    # Determine final password length
    length = secrets.randbelow(max_length - min_length + 1) + min_length

    # Base character set
    characters = list(string.ascii_letters)
    required_chars = []

    # Append digit characters if needed
    if use_numbers:
        characters += list(string.digits)
        if required_types:
            required_chars.append(secrets.choice(string.digits))

    # Append special characters if needed
    if use_special_chars:
        characters += list(string.punctuation)
        if required_types:
            required_chars.append(secrets.choice(string.punctuation))

    # Ensure at least one letter is included
    if required_types:
        required_chars.append(secrets.choice(string.ascii_letters))

    # Fill the rest of the password
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(characters) for _ in range(remaining_length)]

    # Shuffle the password
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)


def main():
    try:
        min_length = int(input("Enter minimum password length: "))
        max_length = int(input("Enter maximum password length: "))
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"

        password = generate_password(min_length, max_length, use_numbers, use_special_chars)
        print("Generated password:", password)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
