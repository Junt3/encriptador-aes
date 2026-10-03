from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import getpass  # Librería estándar para ocultar la contraseña al escribirla

def generate_key(password: str, salt: bytes):
    """Genera una clave a partir de una contraseña y una sal"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(input_file: str, output_file: str, password: str):
    """Cifra un archivo con AES-CBC"""
    salt = os.urandom(16)
    key = generate_key(password, salt)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f:
        file_data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(salt + iv + encrypted_data)

    print(f"\n✅ ¡Éxito! Archivo cifrado guardado en: {output_file}")

def decrypt_file(input_file: str, output_file: str, password: str):
    """Descifra un archivo cifrado con AES-CBC"""
    try:
        with open(input_file, 'rb') as f:
            salt = f.read(16)
            iv = f.read(16)
            encrypted_data = f.read()

        key = generate_key(password, salt)

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

        print(f"\n✅ ¡Éxito! Archivo descifrado guardado en: {output_file}")
        
    except ValueError:
        # Captura el error si la contraseña es incorrecta o el archivo fue alterado
        print("\n❌ ERROR: Contraseña incorrecta o el archivo está dañado.")
    except Exception as e:
        print(f"\n❌ ERROR inesperado: {e}")

def main():
    while True:
        print("\n" + "="*30)
        print("   MENÚ DE CRIPTOGRAFÍA AES")
        print("="*30)
        print("1. Encriptar un archivo")
        print("2. Desencriptar un archivo")
        print("3. Salir")
        print("="*30)
        
        opcion = input("Elige una opción (1/2/3): ").strip()

        if opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        if opcion not in ['1', '2']:
            print("❌ Opción no válida. Por favor, elige 1, 2 o 3.")
            continue

        # Pedir la ruta del archivo (puedes arrastrar el archivo a la consola)
        input_file = input("\nIntroduce la ruta del archivo (o arrástralo aquí): ").strip()
        
        # Eliminar comillas si el usuario arrastra el archivo y la ruta tiene espacios
        input_file = input_file.strip("'\"")

        if not os.path.exists(input_file):
            print(f"❌ ERROR: No se pudo encontrar el archivo '{input_file}'. Verifica la ruta.")
            continue

        # Pedir la contraseña sin mostrarla en pantalla
        password = getpass.getpass("Introduce la contraseña: ")

        if opcion == '1':
            # Genera un nombre automático para el archivo cifrado
            output_file = input_file + '.enc'
            print(f"\nProcesando... Cifrando '{input_file}'")
            encrypt_file(input_file, output_file, password)
            
        elif opcion == '2':
            # Pedir al usuario cómo quiere llamar al archivo recuperado
            print("Ejemplo de nombre de salida: documento_recuperado.txt")
            output_file = input("Introduce el nombre del archivo resultante (con su extensión): ").strip()
            print(f"\nProcesando... Descifrando '{input_file}'")
            decrypt_file(input_file, output_file, password)

# Punto de entrada del programa
if __name__ == "__main__":
    main()