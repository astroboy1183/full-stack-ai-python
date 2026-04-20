'''
Challenge: Secret Message Encryptor & Decryptor (Building a Caesar Cipher)

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
     Ask for a message and a numeric secret key.
     Use a Caesar Cipher (shift letters by the key value).
     Output the encrypted message.
3. If decrypting:
     Ask for the encrypted message and key.
     Reverse the encryption to get the original message.

Rules:
Only encrypt letters; leave spaces and punctuation as-is.
Make sure the letters **wrap around** (e.g., 'z' + 1 → 'a').


Bonus:
Allow uppercase and lowercase letter handling.
Show a clean interface.
'''
import string

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, key):
    return encrypt(encrypted_message, -key)

if __name__ == "__main__":
    print("Secret Message Encryptor & Decryptor")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().lower()

    if choice == "e":
        message = input("Enter your message: ")
        key = int(input("Enter the secret key: "))
        encrypted_message = encrypt(message, key)
        print("Encrypted message:", encrypted_message)
    elif choice == "d":
        encrypted_message = input("Enter the encrypted message: ")
        key = int(input("Enter the secret key: "))
        decrypted_message = decrypt(encrypted_message, key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Exiting.")
        exit()

    print("Thanks for using the Secret Message Encryptor & Decryptor!")
