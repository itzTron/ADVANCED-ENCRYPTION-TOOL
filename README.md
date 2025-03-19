# File Encryptor GUI (AES-256)
*COMPANY*: CODTECH IT SOLUTIONS |
*NAME*: TANMOY NASKAR |
*INTERN ID*: CT08VMU |
*DOMAIN*: Cyber Security & Ethical Hacking. | 
*DURATION*: 4 WEEKS |
*MENTOR*: NEELA SANTOSH |

This is a Python-based AES-256 file encryption and decryption GUI application built using GTK (PyGObject). It allows users to encrypt and decrypt files securely using AES-256 encryption, with encryption keys stored in an SQLite database.

## Features
- AES-256 encryption using CBC mode
- Secure key storage in SQLite database
- File encryption with automatic deletion of the original file
- File decryption with automatic removal of the encrypted file
- GTK-based GUI for easy file selection and encryption/decryption operations

## Prerequisites
Ensure you have the following dependencies installed before running the application.

### Install Required Packages (Linux - Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-gi python3-gi-cairo gir1.2-gtk-3.0
pip install cryptography
```

### Install Required Packages (Arch Linux)
```bash
sudo pacman -S python python-pip python-gobject gtk3
pip install cryptography
```

### Install Required Packages (MacOS - Requires Homebrew)
```bash
brew install python3 gtk+3 pygobject3
pip3 install cryptography
```

> **Note:** Windows users will need to install GTK separately. It is recommended to use WSL (Windows Subsystem for Linux) or a Linux-based environment for best compatibility.

## Installation
### Clone the Repository
```bash
https://github.com/itzTron/ADVANCED-ENCRYPTION-TOOL.git
```

## Running the Application
```bash
python3 file_encryptor_app.py
```

## Usage
1. Open the application.
2. Select a file to encrypt or decrypt using the file chooser.
3. Click the "Encrypt File" button to encrypt the selected file.
4. Click the "Decrypt File" button to decrypt an already encrypted file.
5. The status label will display the encryption or decryption status.
## Example Image:
![Image](https://github.com/user-attachments/assets/7660857e-1e2e-4e99-bb31-0ac73fc89178)

## Troubleshooting
- If you encounter `ModuleNotFoundError: No module named 'gi'`, install the required GTK bindings using the installation steps above.
- Ensure the `cryptography` library is installed using `pip install cryptography`.

## License
This project is licensed under the MIT License. Feel free to modify and distribute.

## Author
Developed by Tanmoy Naskar 

