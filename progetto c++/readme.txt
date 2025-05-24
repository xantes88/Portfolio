Simple CRM System in C++
A command-line based Customer Relationship Management (CRM) application written in C++ to manage customer records, track interactions, and persist data to a file. It supports adding, editing, deleting, searching customers, and recording customer interactions.

Features
Add Customer: Input and validate customer ID, full name (first and last name), and email address.

View Customers: Display all customers along with their recorded interactions.

Edit Customer: Modify existing customer details with validation.

Delete Customer: Remove customers by their ID.

Search Customers: Search customers by first or last name.

Add Interaction: Log interactions related to customers.

Data Persistence: Save and load customer data and interactions from a text file (crm_data.txt).

Validation Rules
Customer Name: Must contain exactly two parts (first and last name) separated by a single space; letters only.

Email: Must contain @ symbol and domain ending with .com.

Customer ID: Must be an integer.

Getting Started
Prerequisites
A C++ compiler supporting C++11 or later (e.g., g++, clang++, Visual Studio).

Compilation
bash
Copia
Modifica
g++ -std=c++11 -o crm_app crm.cpp
Running
bash
Copia
Modifica
./crm_app
Usage
Upon running the program, you will see a menu with the following options:

Add Customer – Add new customer data.

View Customers – Show all customers and their interactions.

Edit Customer – Update an existing customer’s details.

Delete Customer – Remove a customer by ID.

Search Customer – Search by name or surname.

Add Interaction – Add notes or details for a specific customer.

Save and Exit – Save all data to crm_data.txt and exit the program.

File Format (crm_data.txt)
Each customer record is stored on a separate line:

php-template
Copia
Modifica
<ID>,<Full Name>,<Email>
Interactions related to the customer follow immediately with lines starting with:

javascript
Copia
Modifica
interaction:<interaction details>
Code Structure
Customer struct: Stores customer ID, full name, email, and a list of interactions.

Input Validation: Functions to validate names and emails.

CRUD Functions: Add, view, edit, delete customers and add interactions.

File I/O: Save and load customer data including interactions.

Known Limitations
Email validation is basic and only checks for .com domains.

The data file format is simple and not optimized for large data sets.

No concurrency or multi-user support.

