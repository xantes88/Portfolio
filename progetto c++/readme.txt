🧩 CRM CLI Manager – C++ Customer & Interaction Tracker

🧾 Overview

This project is a command-line based CRM system (Customer Relationship Management) developed in modern C++.
It allows you to create, edit, track, and persist customer records, including a detailed log of customer interactions — directly from the terminal.

Designed for simplicity, extensibility, and real-world learning, this application demonstrates core C++ principles and simulates a lightweight CRM experience without external libraries or databases.

⚙️ Features
📇 Add new customers with ID, validated name, and email

🔍 Search customers by first or last name

📝 Edit and update customer records

❌ Remove customers by ID

💬 Track and log customer interactions

💾 Save and load all data to/from a local text file

🔐 Input validation and data integrity checks (name, email, ID)

🗃️ File Structure

📁 crm-cli/
├── main.cpp            # Main application logic
├── crm_data.txt        # Data file (auto-generated)
└── README.md           # Documentation
🚀 Getting Started
Compile the program using g++ or any C++ compiler:

g++ -o crm main.cpp
Run the executable:


./crm
Follow the CLI menu to manage your customers and their interactions.

All data is saved in crm_data.txt after exiting the application.

📈 Business Value
This project simulates the core workflow of a CRM, making it highly relevant for:

Small business management tools

Internal customer tracking systems

Onboarding to larger CRM logic (e.g., Salesforce, HubSpot)

🚀 Why It Matters:
Teaches user-centric design for real operations (sales, support, etc.)

Shows understanding of data validation, persistence, and I/O

Can be the backend logic for a GUI desktop app or web-connected CRM

🧠 Technical Concepts
Standard C++ (no external libraries)

struct usage to model customer entities

std::vector, std::string, std::getline, std::fstream

Input validation (name parsing, email syntax, numeric ID check)

Data persistence using a flat .txt file

Console menu with loop control and input sanitization

📌 Future Improvements

Migrate storage to JSON or SQLite

Add unit tests and modularize codebase

Build GUI frontend (e.g. Qt or wxWidgets)

Add login/auth system

Export interactions to report format (CSV or PDF)

🔒 Validation Logic

The app validates:

Name: must include one space, and only letters

Email: must contain @ and end with .com

ID: must be a valid integer


