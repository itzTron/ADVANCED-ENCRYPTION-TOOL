# AES-256 File Encryptor GUI

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
git clone https://github.com/yourusername/aes-gui-encryptor.git
cd aes-gui-encryptor
```

## Running the Application
```bash
python3 aes_gui.py
```

## Usage
1. Open the application.
2. Select a file to encrypt or decrypt using the file chooser.
3. Click the "Encrypt File" button to encrypt the selected file.
4. Click the "Decrypt File" button to decrypt an already encrypted file.
5. The status label will display the encryption or decryption status.

## Troubleshooting
- If you encounter `ModuleNotFoundError: No module named 'gi'`, install the required GTK bindings using the installation steps above.
- Ensure the `cryptography` library is installed using `pip install cryptography`.

## License
This project is licensed under the MIT License. Feel free to modify and distribute.

## Author
Developed by Tanmoy Nasar 

