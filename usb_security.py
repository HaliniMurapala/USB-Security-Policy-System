```python
import os
import subprocess
from tkinter import *
from tkinter import simpledialog, messagebox

# Global variables
password = ""
password_file = "secure_password.txt"

def save_password(password):
    with open(password_file, "w") as file:
        file.write(password)

def load_password():
    with open(password_file, "r") as file:
        return file.read()

def hide_files():
    # Hide the password file
    subprocess.run(["attrib", "+h", password_file])

def unhide_files():
    # Unhide the password file
    subprocess.run(["attrib", "-h", password_file])

def disable_usb():
    global password

    password = simpledialog.askstring("Set Password", "Set password to disable USB:", show="*")

    if password:
        save_password(password)

        disable_cmd = 'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR" /v "Start" /t REG_DWORD /d 4 /f'
        subprocess.run(disable_cmd, shell=True)

        messagebox.showinfo("USB Control", "USB disabled successfully.\nPassword is set!")
    else:
        messagebox.showwarning("Password Not Set", "Password not set. USB not disabled!")

def enable_usb():
    global password

    saved_password = load_password()

    entered_password = simpledialog.askstring("Enable USB", "Enter the password to enable USB:", show="*")

    if entered_password == saved_password:
        enable_cmd = 'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR" /v "Start" /t REG_DWORD /d 3 /f'
        subprocess.run(enable_cmd, shell=True)

        messagebox.showinfo("USB Control", "USB enabled successfully!")
    else:
        messagebox.showwarning("Invalid Password", "Incorrect password. USB not enabled!")

# Unhide the files before creating the GUI window
unhide_files()

# Create the GUI window
window = Tk()
window.geometry("300x200")

# Disable USB Button
disable_button = Button(window, text="Disable USB", command=disable_usb)
disable_button.pack(pady=20)

# Enable USB Button
enable_button = Button(window, text="Enable USB", command=enable_usb)
enable_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()

# Hide the files after the program completes
hide_files()
