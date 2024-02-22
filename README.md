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

#### Making an .exe using Nuitka

[Nuitka](https://nuitka.net/) is a Python compiler that can compile Python code into native machine code, including creating standalone executables. Follow these steps to compile the Password Manager application into an .exe file using Nuitka:

1. Install Nuitka:

   ```
   pip install nuitka
   ```
   
1.2. Navigate to the directory containing the `management.py` file.

1.3. Run the following command to compile the Python code into an executable:
   
   ```
   python -m nuitka --recurse-all --follow-imports management.py
   ```

This command compiles the `management.py` script along with all its dependencies into a standalone executable.

1.4. Once the compilation process is complete, you will find the generated executable file in the `./dist` directory.

1.5. You can now run the Password Manager application by double-clicking on the generated .exe file.

Note: Depending on your operating system and configuration, you may need to grant appropriate permissions to run the executable.

2. (Second option) Run the application:

   ```
   python password_manager.py
   ```

3. Log in with the default credentials:

   ```
   Login: admin
   Password: admin
   ```

4. Change to your own login and password please.
5. Use the interface to manage your passwords securely.

### Contribution

Contributions are welcome! Feel free to open issues or pull requests to suggest improvements, report bugs, or add new features to the application.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
