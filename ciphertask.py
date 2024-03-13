#!/usr/bin/env python3
#!/usr/bin/env python3

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                offset = ord('A')
            else:
                offset = ord('a')
            shifted = (ord(char) - offset + shift * mode) % 26 + offset
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    print("╔════════════════════════════════════════════════╗")
    print("║                Welcome to RJBYTES              ║")
    print("║               Caesar Cipher Tool                ║")
    print("╚════════════════════════════════════════════════╝")

    while True:
        choice = input("\nDo you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        text = input("Enter the text: ")
        shift = int(input("Enter the shift value (an integer): "))

        if choice == 'e':
            encrypted_text = caesar_cipher(text, shift, 1)
            print("\nEncrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, -shift, -1)  # Decrypt using negative shift
            print("\nDecrypted text:", decrypted_text)

        another = input("\nDo you want to perform another operation? (yes/no): ").lower()
        if another in ['yes', 'y']:
            continue
        else:
            print("Thank you for using the Caesar Cipher Tool. Goodbye!")
            break

if __name__ == "__main__":
    main()

