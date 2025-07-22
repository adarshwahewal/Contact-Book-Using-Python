# 📇 Contact Book (Python + MySQL)

A simple command-line based Contact Book application built using **Python** and **MySQL**.  
It allows users to **add**, **view**, **search**, and **delete** contact details through an interactive menu in the terminal.

---

## 🚀 Features

- Add new contacts (Name, Phone, Email)
- Display all saved contacts
- Search for a contact by name
- Delete contact from the database
- Menu-driven CLI interface

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Database**: MySQL
- **Library**: mysql-connector-python

---

## ⚙️ Setup Instructions

### 1. Create MySQL Database & Table

```sql
CREATE DATABASE contact_book;

USE contact_book;

CREATE TABLE contacts (
  name VARCHAR(50),
  phone VARCHAR(15),
  email VARCHAR(100)
);
````

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/contact-book.git
cd contact-book
```

### 3. Install Required Package

```bash
pip install mysql-connector-python
```

### 4. Update Database Credentials

Edit the `get_connection()` function in `main.py` with your MySQL username and password.

```python
user='root',
password='your_mysql_password'
```

### 5. Run the Script

```bash
python main.py
```

---

## 🧪 Sample Output

```
1. Add Contact
2. Display Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter choice:
```

---

## 👨‍💻 Author

**Adarsh Wahewal**
B.Tech Computer Science & Engineering
Python | SQL | Power BI | Excel

---

## 📌 Note

* Make sure MySQL server is running.
* Passwords should be managed securely in production using `.env` files or credential managers.




