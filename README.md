## Password Manager Application

This repository contains a simple password manager application implemented in Python using the Tkinter library for the graphical user interface (GUI), SQLite for the database management, and the cryptography library for encryption and decryption of passwords.

### Features

- **Secure Password Storage**: Passwords are stored in an SQLite database and encrypted using the Fernet symmetric encryption algorithm from the cryptography library.
- **User Authentication**: Users can log in using a username and password. Default login credentials are provided for initial access to the application.
- **Password Management**: Users can add, retrieve, and update passwords for different services within the application.
- **Change Login Credentials**: Users can change their login credentials securely within the application.

### Requirements

To run the application, you need to have Python installed on your system along with the following libraries:

- `tkinter`: Used for building the GUI.
- `cryptography`: Used for encryption and decryption of passwords.
- `sqlite3`: Used for database management.

### Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your_username/password-manager.git
   ```

2. Install the required Python libraries:

   ```
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:

   ```
   python password_manager.py
   ```

2. Log in with the default credentials:

   ```
   Login: admin
   Password: admin
   ```

3. Change to your own login and password please.
4. Use the interface to manage your passwords securely.

### Contribution

Contributions are welcome! Feel free to open issues or pull requests to suggest improvements, report bugs, or add new features to the application.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
