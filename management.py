import os
import sqlite3
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Function to generate encryption key
def generate_key():
    return Fernet.generate_key()

# Function to load encryption key from file or generate a new one
def load_or_generate_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            key = f.read()
    else:
        key = generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    return Fernet(key)

# Function to encrypt password
def encrypt_password(password, cipher_suite):
    return cipher_suite.encrypt(password.encode()).decode()

# Function to decrypt password
def decrypt_password(encrypted_password, cipher_suite):
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

# Initialize Key Management System (KMS)
def initialize_kms():
    key_file = 'encryption_key.key'
    cipher_suite = load_or_generate_key(key_file)
    return cipher_suite

# Function to add password
def add_password():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if service and username and password:
        encrypted_password = encrypt_password(password, cipher_suite)
        c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)", (service, username, encrypted_password))
        conn.commit()
        messagebox.showinfo("Success", "Password added successfully!")
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

# Function to get password
def get_password():
    service = service_entry.get()
    c.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
    result = c.fetchone()
    if result:
        decrypted_password = decrypt_password(result[1], cipher_suite)
        messagebox.showinfo("Password", f"Username: {result[0]}\nPassword: {decrypted_password}")
    else:
        messagebox.showwarning("Error", "Password not found.")

# Function to change password
def change_password():
    service = service_entry.get()
    new_password = password_entry.get()

    if service and new_password:
        encrypted_new_password = encrypt_password(new_password, cipher_suite)
        c.execute("UPDATE passwords SET password=? WHERE service=?", (encrypted_new_password, service))
        conn.commit()
        messagebox.showinfo("Success", "Password changed successfully!")
    else:
        messagebox.showwarning("Error", "Please enter both the service and new password.")

# Function to handle login
def login():
    entered_username = username_entry_login.get()
    entered_password = password_entry_login.get()

    # Fetch encrypted login credentials from the database
    c.execute("SELECT username, password FROM login")
    result = c.fetchone()
    if result:
        decrypted_username = decrypt_password(result[0], cipher_suite)
        decrypted_password = decrypt_password(result[1], cipher_suite)
        if entered_username == decrypted_username and entered_password == decrypted_password:
            # If login successful, show the main window
            login_window.withdraw()
            window.deiconify()
            change_login_button_main.config(state=tk.NORMAL)  # Enable change login credentials button
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    else:
        messagebox.showerror("Login Failed", "No login credentials found")

# Function to change login credentials
def change_login_credentials():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    if new_username and new_password:
        encrypted_new_username = encrypt_password(new_username, cipher_suite)
        encrypted_new_password = encrypt_password(new_password, cipher_suite)
        c.execute("UPDATE login SET username=?, password=?", (encrypted_new_username, encrypted_new_password))
        conn.commit()
        messagebox.showinfo("Success", "Login credentials changed successfully!")
    else:
        messagebox.showwarning("Error", "Please fill in both the new username and password.")

# Function to open the change login window
def open_change_login_window():
    change_login_window.deiconify()
    change_login_window.lift()

# Initialize Key Management System
cipher_suite = initialize_kms()

# Database initialization
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (id INTEGER PRIMARY KEY, service TEXT, username TEXT, password TEXT)''')

# Create table for login credentials if not exists
c.execute('''CREATE TABLE IF NOT EXISTS login
             (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

# Create default login credentials if not exists
c.execute("SELECT * FROM login")
if not c.fetchone():
    default_username = "admin"
    default_password = "admin"
    encrypted_default_username = encrypt_password(default_username, cipher_suite)
    encrypted_default_password = encrypt_password(default_password, cipher_suite)
    c.execute("INSERT INTO login (username, password) VALUES (?, ?)", (encrypted_default_username, encrypted_default_password))
    conn.commit()

# Create Tkinter window for login
login_window = tk.Tk()
login_window.title("Login")

# Labels and entry fields for login
username_label_login = tk.Label(login_window, text="Username:")
username_label_login.grid(row=0, column=0, padx=10, pady=5)
username_entry_login = tk.Entry(login_window)
username_entry_login.grid(row=0, column=1, padx=10, pady=5)

password_label_login = tk.Label(login_window, text="Password:")
password_label_login.grid(row=1, column=0, padx=10, pady=5)
password_entry_login = tk.Entry(login_window, show="*")
password_entry_login.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(login_window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Hide the main window until login is successful
window = tk.Tk()
window.title("Password Manager")
window.withdraw()

# Labels and entry fields for main window
service_label = tk.Label(window, text="Service:")
service_label.grid(row=0, column=0, padx=10, pady=5)
service_entry = tk.Entry(window)
service_entry.grid(row=0, column=1, padx=10, pady=5)

username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5)
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons for main window
add_button = tk.Button(window, text="Add Password", command=add_password)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

get_button = tk.Button(window, text="Get Password", command=get_password)
get_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

change_button = tk.Button(window, text="Change Password", command=change_password)
change_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Button to open the change login window
change_login_button_main = tk.Button(window, text="Change Login Credentials", command=open_change_login_window)
change_login_button_main.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Create Tkinter window for changing login credentials
change_login_window = tk.Tk()
change_login_window.title("Change Login Credentials")
change_login_window.withdraw()  # Hide the window initially

# Labels and entry fields for changing login credentials
new_username_label = tk.Label(change_login_window, text="New Username:")
new_username_label.grid(row=0, column=0, padx=10, pady=5)
new_username_entry = tk.Entry(change_login_window)
new_username_entry.grid(row=0, column=1, padx=10, pady=5)

new_password_label = tk.Label(change_login_window, text="New Password:")
new_password_label.grid(row=1, column=0, padx=10, pady=5)
new_password_entry = tk.Entry(change_login_window, show="*")
new_password_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to change login credentials in the change login window
change_login_button = tk.Button(change_login_window, text="Change Login Credentials", command=change_login_credentials)
change_login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Run Tkinter event loop for login window
login_window.mainloop()
