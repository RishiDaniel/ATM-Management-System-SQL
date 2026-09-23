# ATM-Management-System-SQL
A non-GUI ATM management system built using Python and MySQL, featuring account management, balance inquiry, withdrawals, deposits, PIN changes, and fund transfers.
# ATM Management System 💳

A simple **Non-GUI ATM Management System** developed using **Python and MySQL**.

This project was created as a **Class 11 programming project** to practice Python programming along with database connectivity and SQL operations.

## 🚀 Features

* 👤 User account management
* 🔐 PIN-based login
* 💰 Balance inquiry
* 💸 Cash withdrawal
* 💵 Cash deposit
* 🔄 Fund transfer
* 🔑 PIN change
* 🗄️ MySQL database storage

## 🛠️ Technologies Used

* **Python 3**
* **MySQL**
* **MySQL Connector for Python**
* SQL
* Functions
* Loops
* Conditional statements
* Database queries

## 📂 Project Structure

```text
ATM-Management-System-SQL/
│
├── atm.py
├── database.sql
└── README.md
```

## 🗄️ Database

The project uses **MySQL** to store and manage ATM account information.

Example information stored in the database:

* Account/User name
* PIN
* Account balance
* Transaction-related information

Python connects to MySQL using the MySQL Connector library.

## ⚙️ Setup

### 1. Install Python

Install Python 3 on your computer.

### 2. Install MySQL

Install MySQL Server and MySQL Workbench.

### 3. Install MySQL Connector

Open Command Prompt or Terminal and run:

```bash
pip install mysql-connector-python
```

### 4. Create the Database

Open MySQL Workbench and run the SQL commands from:

```text
database.sql
```

### 5. Configure Database Connection

Update the MySQL connection details in the Python program according to your MySQL setup.

For example:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="atm"
)
```

### 6. Run the Program

Open the project folder and run:

```bash
python atm.py
```

## 📋 ATM Operations

```text
1. Balance Inquiry
2. Withdraw
3. PIN Change
4. Fund Transfer
5. Cash Deposit
6. Exit
```

## 🧠 Concepts Learned

This project helped me practice:

* Python functions
* Variables and data types
* `if-else` statements
* `while` loops
* User input
* Exception handling
* SQL queries
* MySQL databases
* Python-MySQL connectivity
* Basic database management

## 🔮 Future Improvements

* Add transaction history
* Add account creation through the Python interface
* Add better input validation
* Add transaction receipts
* Add logout functionality
* Add GUI using Tkinter
* Improve database security
* Add separate admin functionality

## ⚠️ Disclaimer

This is an **educational project** created for learning Python and MySQL. It is not designed for real banking or financial transactions.

Do not use real passwords, PINs, bank account numbers, or other sensitive information in this project.

## 🎓 Project Information

**Project:** ATM Management System
**Type:** Python + MySQL
**Interface:** Non-GUI / Console
**Academic Level:** Class 11
**Author:** Rishi Daniel

---

⭐ If you find this project useful, feel free to star the repository!
