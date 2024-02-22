# Password Manager Application

Description:

This is a simple password manager application built using Python's Tkinter library. The application allows users to store and manage their passwords for different websites securely. It features functionalities such as adding, searching, and deleting passwords, as well as generating secure passwords.

Features:

Password Generation: Users can generate secure passwords using a combination of letters, numbers, and symbols.
Password Storage: Users can store passwords for different websites along with their associated email addresses.
Password Search: Users can search for saved passwords by entering their username and the website.
Password Deletion: Users can delete saved passwords for specific websites.
New User Registration: New users can register by providing their name, website, email, and password.
Instructions:

Installation:

Make sure you have Python installed on your system.

Install the required dependencies using pip:

    pip install tk

Usage:

Run the script password_manager.py.

Enter your username, website, email, and password to add a new password entry.

Click on the "Search" button to find a saved password.

Click on the "Generate Password" button to create a secure password.

Click on the "Add" button to save the entered details.

Click on the "Delete" button to remove a saved password entry.

Click on the "NEW USER" button to register as a new user.

Security Key:

To ensure security, the application prompts for a security key when deleting or searching for passwords.
The security key is required to access sensitive information stored in the application.
Files:

password_manager.py: Main Python script containing the application code.

Data.json: JSON file to store password data.

security_data.json: JSON file to store security keys.
