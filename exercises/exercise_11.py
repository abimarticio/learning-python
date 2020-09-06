# Ceaser Cipher

from string import ascii_uppercase

def get_alphabet() -> list:
    letters= list(ascii_uppercase)
    return letters

def encrypt_decrypt_text(text: str, alphabet: list, mode: str = "encrypt", key: int = 1) -> str:
    alphabet_len = len(alphabet)
    text = text.upper()
    output_text = []
    for letter in text:
        letter_index = alphabet.index(letter)
        if mode == "encrypt":
            output_index = (letter_index + key) % alphabet_len
        elif mode == "decrypt":
            output_index = (letter_index - key) % alphabet_len
        output_letter = alphabet[output_index]
        output_text.append(output_letter)
    return "".join(output_text)

def main():
    mode = input("Do you want to encrypt or decrypt? ")
    mode = mode.lower()
    alphabet = get_alphabet()
    if mode == "encrypt":
        user_input = input("Enter text you want to encrypt: ")
        shift = int(input("Key: "))
        encrypted_text = encrypt_decrypt_text(text=user_input, mode=mode, alphabet=alphabet, key=shift)
        print(encrypted_text)
    elif mode == "decrypt":
        user_input = input("Enter text you want to decrypt: ")
        shift = int(input("Key: "))
        decrypted_text = encrypt_decrypt_text(text=user_input, mode=mode, alphabet=alphabet, key=shift)
        print(decrypted_text)
    else:
            raise ValueError

main()