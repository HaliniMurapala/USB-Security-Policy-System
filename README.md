# USB Security Policy System

A Python based desktop application I built during my 
internship that allows administrators to control USB 
storage access on Windows systems. The tool uses a 
simple GUI and password protection to prevent 
unauthorized USB devices from being used.

---

## Why I Built This

In organizations, unauthorized USB drives are a major 
security threat. People can steal data or introduce 
malware using USB drives. I wanted to build a simple 
tool that gives administrators control over who can 
use USB storage on a Windows system.

---

## What It Does

- Disables USB storage access on Windows with one click
- Password protects the enable/disable functionality
- Saves password securely in a hidden file
- Re-enables USB only when correct password is entered
- Simple and clean GUI built with Python Tkinter
- Works silently in the background

---

## How It Works

When you run the program:
- A simple window opens with two buttons
- Disable USB — asks you to set a password
  then disables all USB storage on the system
- Enable USB — asks for the password
  if correct it re-enables USB storage
- Password file is automatically hidden
  when program closes

The tool works by modifying the Windows Registry:
- USBSTOR Start = 4 means USB storage disabled
- USBSTOR Start = 3 means USB storage enabled

---

## Technologies Used

- Python 3
- Tkinter — GUI development
- Subprocess — running system commands
- Windows Registry — USB control
- attrib command — file hiding

---

## Requirements

- Windows OS only
- Python 3.x
- Must run as Administrator

---

## How to Run

Step 1 — Install Python 3 from python.org

Step 2 — Run as Administrator:
- Right click on usb_security.py
- Click "Run as Administrator"

Step 3 — Use the GUI:
- Click "Disable USB" to block USB storage
- Set a password when prompted
- Click "Enable USB" to restore access
- Enter password when prompted

---

## Project Structure

USB-Security-Policy-System/
├── usb_security.py     → Main application file
└── README.md
## Known Limitations

- Works on Windows only
- Password is stored as plain text
- Requires Administrator privileges

## Future Improvements

- Encrypt password using hashlib
- Add logging of USB connection attempts
- Support for Linux using pyudev
- Email alert when unauthorized USB is detected
