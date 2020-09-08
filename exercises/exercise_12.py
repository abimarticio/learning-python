# atbash cipher

from string import ascii_uppercase

def get_alphabet() -> list:
    letters= list(ascii_uppercase)
    return letters

def encrypt_decrypt_text(text: str, alphabet: list) -> str:
    alphabet_len = len(alphabet)
    text = text.upper()
    output_text = []
    for letter in text:
        letter_index = alphabet.index(letter) 
        output_index = ((alphabet_len - 1) * letter_index + (alphabet_len - 1)) % alphabet_len
        output_letter = alphabet[output_index]
        output_text.append(output_letter)
    return "".join(output_text)

def main():
    while True:
        user_input = input("Enter text you want to encrypt or decrypt: ")
        if user_input != "":
            break
        elif user_input == "":
            continue
    alphabet = get_alphabet()
    encrypted_decrypted_text = encrypt_decrypt_text(text=user_input, alphabet=alphabet)
    print(encrypted_decrypted_text)
main()

