import base64 import os from Crypto.Cipher import AES from Crypto.Random import get_random_bytes from hashlib import sha256 import json from PIL import Image import piexif import tempfile

========= Custom Mapping (You define this) =========

custom_map = { # === YOUR CUSTOM MAPPING START === # 'A': '|•', 'B': 'πx', ... # === YOUR CUSTOM MAPPING END === } reverse_custom_map = {v: k for k, v in custom_map.items()}

========= Padding Utilities =========

def pad(data): length = 16 - (len(data) % 16) return data + bytes([length]) * length

def unpad(data): return data[:-data[-1]]

========= Custom Encryption Layer =========

=== CUSTOM ENCRYPTION START ===

def custom_encrypt(data): # Your custom logic to convert data using custom_map for k, v in custom_map.items(): data = data.replace(k.encode(), v.encode()) return data

=== CUSTOM ENCRYPTION END ===

=== CUSTOM DECRYPTION START ===

def custom_decrypt(data): # Your custom logic to reverse conversion using reverse_custom_map for v, k in reverse_custom_map.items(): data = data.replace(v.encode(), k.encode()) return data

=== CUSTOM DECRYPTION END ===

========= AES Layer =========

def aes_encrypt(data, password): key = sha256(password.encode()).digest() iv = get_random_bytes(16) cipher = AES.new(key, AES.MODE_CBC, iv) encrypted = cipher.encrypt(pad(data)) return base64.b64encode(iv + encrypted)

def aes_decrypt(data, password): key = sha256(password.encode()).digest() raw = base64.b64decode(data) iv = raw[:16] cipher = AES.new(key, AES.MODE_CBC, iv) decrypted = unpad(cipher.decrypt(raw[16:])) return decrypted

========= File Utilities =========

def read_file_bytes(path): with open(path, 'rb') as f: return f.read()

def write_file_bytes(path, data): with open(path, 'wb') as f: f.write(data)

========= Metadata Removal =========

def remove_metadata(file_path): try: img = Image.open(file_path) data = list(img.getdata()) img_no_exif = Image.new(img.mode, img.size) img_no_exif.putdata(data) temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") img_no_exif.save(temp_file.name) return temp_file.name except: return file_path

========= Main Terminal Interface =========

def main(): while True: choice = input("Choose mode (1: Encrypt, 2: Decrypt, 0: Exit): ") if choice == '0': break

method = input("Type (1: Text, 2: File): ")
    password = input("Enter password: ")

    if method == '1':  # Text
        if choice == '1':
            text = input("Enter text to encrypt: ")
            custom = custom_encrypt(text.encode())
            encrypted = aes_encrypt(custom, password)
            print("Encrypted:", encrypted.decode())
        else:
            enc_text = input("Paste encrypted text: ")
            try:
                decrypted = aes_decrypt(enc_text.encode(), password)
                plain = custom_decrypt(decrypted)
                print("Decrypted:", plain.decode())
            except:
                print("Decryption failed.")

    elif method == '2':  # File
        file_path = input("Enter file path: ")
        if not os.path.isfile(file_path):
            print("File not found.")
            continue
        output_name = input("Enter output file name: ")

        if choice == '1':
            cleaned_path = remove_metadata(file_path)
            raw = read_file_bytes(cleaned_path)
            custom = custom_encrypt(raw)
            encrypted = aes_encrypt(custom, password)
            write_file_bytes(output_name, encrypted)
            print("Encrypted file saved as", output_name)
            if cleaned_path != file_path:
                os.remove(cleaned_path)
        else:
            enc_data = read_file_bytes(file_path)
            try:
                decrypted = aes_decrypt(enc_data, password)
                plain = custom_decrypt(decrypted)
                write_file_bytes(output_name, plain)
                print("Decrypted file saved as", output_name)
            except:
                print("Decryption failed.")

if name == 'main': main()

