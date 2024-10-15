def caesar_cipher(message, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.

    Args:
        message (str): The message to be encrypted or decrypted.
        shift (int): The shift value for the Caesar Cipher.
        mode (str): 'e' for encryption or 'd' for decryption.

    Returns:
        str: The encrypted or decrypted message.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in message:
        if char.isalpha():
            index = alphabet.index(char.lower())
            if mode == 'e':
                new_index = (index + shift) % 26
            elif mode == 'd':
                new_index = (index - shift) % 26
            if char.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += char

    return result


def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            message = input("Enter a message to encrypt: ")
            shift = int(input("Enter a shift value: "))
            encrypted_message = caesar_cipher(message, shift, 'e')
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter a message to decrypt: ")
            shift = int(input("Enter a shift value: "))
            decrypted_message = caesar_cipher(message, shift, 'd')
            print(f"Decrypted message: {decrypted_message}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()