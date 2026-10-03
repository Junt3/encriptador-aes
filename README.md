# 🔐 Encriptador de Archivos AES-256

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Cryptography](https://img.shields.io/badge/Cryptography-Security-red?style=for-the-badge)]()

Herramienta de línea de comandos desarrollada en Python para encriptar y desencriptar archivos de forma segura utilizando el estándar de cifrado avanzado (AES) en modo CBC. Este script está diseñado con buenas prácticas de ciberseguridad, asegurando que los datos sensibles queden completamente inaccesibles sin la contraseña correcta.

## 🚀 Características y Seguridad Integrada

*   **Cifrado Robusto:** Utiliza algoritmos criptográficos estándar de la industria (`AES` simétrico).
*   **Derivación de Claves (PBKDF2):** No usa la contraseña del usuario directamente como llave. Emplea `PBKDF2HMAC` para derivar una clave criptográficamente fuerte a partir de la contraseña introducida.
*   **Salting Aleatorio:** Genera un *salt* (sal) aleatorio usando `os.urandom` para cada cifrado, protegiendo los archivos contra ataques de diccionario y *rainbow tables*.
*   **Ocultamiento de Credenciales:** Implementa la librería `getpass` para que la contraseña no se muestre en pantalla mientras el usuario la digita en la terminal.
*   **Gestión de Archivos:** Crea de forma automática la versión encriptada o desencriptada del archivo, conservando la integridad de la extensión original tras el descifrado.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Librerías:** `cryptography.hazmat.primitives`, `os`, `getpass`

## ⚙️ Instalación y Uso

1.  **Clonar e instalar dependencias:**
    ```bash
    git clone [https://github.com/Junt3/encriptador-aes.git](https://github.com/Junt3/encriptador-aes.git)
    cd encriptador-aes
    pip install -r requirements.txt
    ```

2.  **Ejecutar el script:**
    ```bash
    python Ecriplab.py
    ```

3.  **Flujo de uso:** El programa solicitará la ruta del archivo que deseas proteger, te pedirá que definas una contraseña (que se mantendrá oculta) y generará el archivo cifrado. El proceso inverso requiere la ruta del archivo cifrado y la contraseña original.

---
*Este proyecto demuestra fundamentos sólidos en seguridad informática y manejo seguro de datos con Python.*
