import os
import sqlite3
import base64
import secrets
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

try:
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk
except ImportError:
    print("Error: The 'gi' module is missing. Install it using: sudo apt install python3-gi gir1.2-gtk-3.0")
    sys.exit(1)

DB_FILE = "file_keys.db"

class FileEncryptorGUI(Gtk.Window):
    def __init__(self):
        super().__init__(title="File Encryptor(AES-256)")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.file_chooser = Gtk.FileChooserButton(title="Select a File")
        vbox.pack_start(self.file_chooser, False, False, 0)

        self.encrypt_button = Gtk.Button(label="Encrypt File")
        self.encrypt_button.connect("clicked", self.encrypt_file)
        vbox.pack_start(self.encrypt_button, False, False, 0)

        self.decrypt_button = Gtk.Button(label="Decrypt File")
        self.decrypt_button.connect("clicked", self.decrypt_file)
        vbox.pack_start(self.decrypt_button, False, False, 0)

        self.status_label = Gtk.Label(label="Status: Ready")
        vbox.pack_start(self.status_label, False, False, 0)

        self.create_database()

    def create_database(self):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS keys (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                file_path TEXT UNIQUE,
                                key TEXT
                              )''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def generate_key(self):
        return secrets.token_bytes(32)

    def store_key(self, file_path, key):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            key_b64 = base64.b64encode(key).decode()
            cursor.execute("INSERT OR REPLACE INTO keys (file_path, key) VALUES (?, ?)", (file_path, key_b64))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error storing key: {e}")
        finally:
            conn.close()

    def retrieve_key(self, file_path):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT key FROM keys WHERE file_path = ?", (file_path,))
            result = cursor.fetchone()
            return base64.b64decode(result[0]) if result else None
        except sqlite3.Error as e:
            print(f"Error retrieving key: {e}")
            return None
        finally:
            conn.close()

    def encrypt_file(self, widget):
        file_path = self.file_chooser.get_filename()
        if not file_path or not os.path.isfile(file_path):
            self.status_label.set_text("Status: No valid file selected")
            return

        key = self.generate_key()
        iv = secrets.token_bytes(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()

        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            padded_data = padder.update(data) + padder.finalize()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            
            encrypted_file_path = file_path + ".enc"
            with open(encrypted_file_path, 'wb') as f:
                f.write(iv + encrypted_data)
            
            os.remove(file_path)
            self.store_key(encrypted_file_path, key)
            self.status_label.set_text(f"Status: File encrypted ({encrypted_file_path})")
        except Exception as e:
            self.status_label.set_text(f"Status: Encryption error - {e}")

    def decrypt_file(self, widget):
        encrypted_file_path = self.file_chooser.get_filename()
        if not encrypted_file_path or not os.path.isfile(encrypted_file_path) or not encrypted_file_path.endswith(".enc"):
            self.status_label.set_text("Status: Invalid encrypted file")
            return
        
        original_file_path = encrypted_file_path.replace(".enc", "")
        key = self.retrieve_key(encrypted_file_path)
        
        if key is None:
            self.status_label.set_text("Status: Encryption key not found")
            return
        
        try:
            with open(encrypted_file_path, 'rb') as f:
                iv = f.read(16)
                encrypted_data = f.read()
            
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            unpadder = padding.PKCS7(128).unpadder()
            
            decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
            decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
            
            with open(original_file_path, 'wb') as f:
                f.write(decrypted_data)
            
            os.remove(encrypted_file_path)
            self.status_label.set_text(f"Status: File decrypted ({original_file_path})")
        except Exception as e:
            self.status_label.set_text(f"Status: Decryption error - {e}")

if __name__ == "__main__":
    app = FileEncryptorGUI()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
