# 🧠 CRM System in C++

**Smart Client Relationship Management with Input Validation, Data Persistence, and Interaction Tracking**

---

## 💼 Executive Summary

Customer data is often managed in messy spreadsheets, vulnerable to human error and lacking structure. This project simulates a lightweight but robust **CRM system** entirely written in C++ — enabling reliable customer tracking, email validation, interaction history, and data persistence.

With strict input validation and a file-based storage system, it offers a solid foundation for small businesses or sales teams looking to organize client relationships and interactions in a structured, automated way.

---

## 🔍 Business Scenario

- **Context**: SME sales teams, freelancers, or customer support operations  
- **Problem**: Fragmented data, no client history, error-prone manual processes  
- **Risk**: Missed follow-ups, inconsistent records, reduced client retention  

---

## ✅ Solution

This system allows users to:
- Add new customers with name/email validation
- Search, update, and delete customer records by ID
- Record multiple interactions per client
- Persist and reload data from a text file
- Maintain clean, reliable, and accessible records

---

## 💡 Key Features

| Feature             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| 🔐 Input Validation | First & last name check, `.com` email format, numeric ID enforcement        |
| 📝 Interaction Logs | Each customer has an associated event history                              |
| 💾 File Persistence | Data saved to `crm_data.txt` on exit                                       |
| 🔍 Search Function  | Lookup by name or surname                                                  |
| 🧠 Simple CLI       | Text-based menu for seamless user interaction                              |

---

## 🧩 Technical Architecture

- **Language**: Modern C++  
- **Data Storage**: Local file (`crm_data.txt`)  
- **Libraries**: `<vector>`, `<fstream>`, `<sstream>`, `<limits>`  
- **Paradigm**: Structured programming with `struct`, loops, and file I/O

---

## 📦 Sample Output

Saved content in `crm_data.txt`:

---

## 🧪 How to Run

Compile and run from terminal:

```bash
g++ -o crm crm_system.cpp
./crm

🚀 Business Use Cases

💼 Sales CRM for freelancers and micro-businesses

🛠️ Operational Tool for customer support teams

🎓 Educational Demo in C++ for business automation

📊 Prototype for early-stage CRM automation projects

📈 Future Enhancements

Web UI with C++ REST API (or Python frontend)

SMTP email integration (reminders, follow-ups)

CSV export and Excel compatibility

Cloud sync (e.g. Google Drive or Dropbox)

🔗 Summary for Stakeholders

✔️ Functional and realistic CRM simulation
✔️ Strong data validation and error prevention
✔️ File-based persistence for data longevity
✔️ Readable codebase built for extension
✔️ Business-focused tool with direct practical value

Built for teams that care about structure, speed, and reliability — even without a full-scale CRM platform.
