# 🏢 Stock Management System (Python)

A **desktop-based Stock Management System** built using **Python**, **Tkinter** for the GUI, and **SQLite3** for the database. The system provides separate functionalities for **Admin** and **Employee**, making it easy to manage inventory, suppliers, employees, and billing.

---

## **Features**

### **Admin Panel**
- Add, delete, and update stock items.
- View current stock and check stock details.
- Generate and check bills.
- Add suppliers and manage supplier information.
- Add and delete employee accounts.
- Separate login for admin access.

### **Employee Panel**
- Purchase items from stock.
- Generate bills for customers.
- Save bills for record keeping.
- Separate login for employee access.

---

## **Technologies Used**
- **Python 3.x** – Programming language
- **Tkinter** – GUI library for desktop applications
- **SQLite3** – Lightweight database for storing stock, employee, supplier, and billing data

---

## **Installation**

1. Install **Python 3.x**: [Python Downloads](https://www.python.org/downloads/)

2. Install required libraries (Tkinter and SQLite3 are usually included):
```bash
# Tkinter installation (if not included)
# Linux (Ubuntu/Debian)
sudo apt-get install python3-tk
# Windows and Mac usually include Tkinter by default



How to Run the Project

Clone or download the repository.

Open terminal or command prompt in the project folder.

Run the main Python file:

python main.py


Login as Admin or Employee:

Admin: Full access to manage stock, employees, suppliers, and bills

Employee: Can purchase items and generate bills

Database

The system uses SQLite3 to store:

Stock items

Supplier details

Employee details

Bills and transactions

Usage

Admin logs in to manage inventory, employees, and suppliers.

Employee logs in to sell items and generate bills.

Bills can be saved and retrieved for records.

Author

Sahil Sunil Pakhare
Email: sahilpakhare17@gmail.com

# SQLite3 comes with Python
python -c "import sqlite3; print('SQLite3 is installed')"
