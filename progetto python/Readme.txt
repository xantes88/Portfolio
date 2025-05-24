# 📱 Python Phonebook CLI App

A lightweight and interactive command-line application built in Python for managing personal phone contacts. The project is designed with simplicity, usability, and data persistence in mind, allowing users to handle their contacts efficiently through the terminal.

---

## 📖 Introduction

In the digital age, managing contact information is essential—but often overlooked. While smartphones and apps offer contact management features, not all users want or need complex systems. This project provides a minimal yet effective solution: a contact manager that runs entirely from the command line and stores data in a readable format.

This application was developed as a practice project to reinforce object-oriented design principles and to demonstrate file handling, data validation, and user interaction through the terminal.

---

## 🎯 Objective

The primary goals of this project are:

- ✅ Build a functional phonebook manager using Python.
- ✅ Provide an intuitive CLI interface for contact management.
- ✅ Ensure data persistence using JSON file storage.
- ✅ Practice object-oriented programming (OOP) and structured code organization.
- ✅ Handle user inputs robustly and prevent data duplication.

---

## 🛠 Methodologies Used

### 🔹 Language & Tools
- **Python 3.x**
- **Standard Libraries only**: `json`, `os`, and `input()` for I/O handling

### 🔹 Key Programming Concepts
- **Object-Oriented Programming (OOP)**: While primarily procedural, the structure can be extended into full OOP.
- **Modular Functions**: Separate responsibilities such as reading, writing, validating, and displaying contacts.
- **JSON for Data Storage**: Ensures readable, editable, and persistent contact data.
- **CLI Menu Interface**: Allows users to navigate actions interactively.

### 🔹 Features Implemented
- Add, edit, delete, and search contacts
- View all saved contacts
- Save/load contacts from a `Contacts.json` file
- Input validation and duplicate contact prevention
- Clean error messages and input prompts

---

## ✅ Results

The final application meets the goals of offering:

- A **fully operational** phonebook manager from the terminal.
- Persistent data stored in a clear and editable `.json` format.
- A clean and **intuitive user experience**, accessible even to beginners.
- Clear code structure that’s easy to extend (e.g., future OOP refactoring, file encryption, GUI integration).

### Example Output:

Menu:

View contacts

Add new contact

Edit contact

Remove contact

Search contact

Exit

cpp
Copia
Modifica

### Example Data (`Contacts.json`):

```json
[
  {
    "Name": "Alice",
    "Surname": "Smith",
    "Number": "1234567890"
  }
]


✅ Final Result — Clearly Explained
The final result of this project is a fully functional command-line phonebook application written in Python that allows users to:

🔹 What the App Does:
Store, view, edit, delete, and search contacts

Save all contact data in a human-readable .json file

Prevent duplicate contacts by checking name, surname, and number

Run entirely in the terminal, with no external libraries required

🔹 Key Output:
User-friendly CLI Menu

markdown
Copia
Modifica
Menu:
1. View contacts
2. Add new contact
3. Edit contact
4. Remove contact
5. Search contact
6. Exit
Data stored in JSON format:

json
Copia
Modifica
[
  {
    "Name": "Alice",
    "Surname": "Smith",
    "Number": "1234567890"
  },
  {
    "Name": "Bob",
    "Surname": "Jones",
    "Number": "0987654321"
  }
]
🔹 Summary of Achievements:
🧩 Core functionalities implemented and tested

💾 Persistent data storage using JSON

👤 Interactive terminal interface suitable for beginners

⚙️ Clean, modular, and readable code

🛡️ Basic error handling and input validation
