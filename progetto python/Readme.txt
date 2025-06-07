📞 Phone Book Manager – Python JSON CLI Application
🔍 Overview
This project is a command-line contact manager developed in Python. It provides basic CRUD functionalities (Create, Read, Update, Delete) for managing personal or business contacts using a persistent JSON file as storage.

It serves as a lightweight and extensible base for:

Python automation exercises

Backend logic for address book applications

Data structure manipulation practice (lists, dictionaries, I/O)

🧠 Features
✅ Add new contacts with validation

📖 Display all saved contacts

🔍 Search by first name or surname

📝 Edit existing contacts

❌ Delete contacts by name and surname

💾 Persistent storage using JSON format

🔒 Duplicate prevention logic

🗂️ File Structure
bash
Copia
Modifica
📁 phonebook/
├── Contacts.json          # Persistent data storage
├── phonebook.py           # Main CLI logic
└── README.md              # Documentation
🚀 How to Run
Clone the repository:

bash
Copia
Modifica
git clone https://github.com/yourusername/phonebook.git
cd phonebook
Make sure you have Python 3 installed:

bash
Copia
Modifica
python --version
Run the script:

bash
Copia
Modifica
python phonebook.py
Interact with the menu-driven interface to add/view/search/edit/delete contacts.

💼 Business Value
Although this is a simplified contact management system, it showcases:

Structured procedural programming

User input validation and basic error handling

JSON file manipulation for persistent data storage

CLI-driven UX for productivity tools

Good practice in designing scalable utility scripts (e.g. this could be converted into a REST API or GUI app)

Such logic can be reused or expanded in:

CRM tools

Internal staff directories

Low-code business automations

🛠️ Technologies Used
Python 3.x

JSON for data persistence

Standard libraries: json, os, input/output

✨ Possible Improvements
Add a GUI (e.g. with Tkinter or PyQt)

Export contacts to CSV or Excel

Implement fuzzy search and filters

Add support for contact groups/tags
