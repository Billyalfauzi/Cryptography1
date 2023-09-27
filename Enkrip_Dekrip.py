def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) + shift - ord('a')
            shifted %= 26
            shifted += ord('a')
            if is_upper:
                shifted = chr(shifted).upper()
            else:
                shifted = chr(shifted)
            encrypted_text += shifted
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt_caesar_cipher(text, shift):
    return encrypt_caesar_cipher(text, -shift)


def main():
    while True:
        print("Menu:")
        print("a. Enkripsi Data")
        print("b. Dekripsi Data")
        print("c. Keluar")
        
        choice = input("Pilih opsi (a/b/c): ")
        
        if choice == 'a':
            text = input("Masukkan pesan yang ingin dienkripsi: ")
            shift = int(input("Masukkan jumlah pergeseran: "))
            # Menghapus spasi sebelum enkripsi
            text = text.replace(" ", "")
            encrypted_text = encrypt_caesar_cipher(text, shift)
            print(encrypted_text)
            print()
        elif choice == 'b':
            text = input("Masukkan pesan yang ingin didekripsi: ")
            shift = int(input("Masukkan jumlah pergeseran: "))
            decrypted_text = decrypt_caesar_cipher(text, shift)
            print(decrypted_text)
            print()
        elif choice == 'c':
            print("Terima kasih!")
            break
        else:
            print("Invalid. Silakan pilih a, b, atau c.")

if __name__ == "__main__":
    main()