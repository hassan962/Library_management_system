# 📚 Library Management System

A Django-based web application that allows librarians to manage books, members, and transactions (issuing and returning books). It also integrates with the Frappe public API to import books.

---

## 🚀 Features

- ✅ CRUD operations for Books and Members
- 📖 Issue and return books
- 💰 Track rent fees and outstanding debts
- 🔍 Search books by title or author
- 🌐 Import books from [Frappe Library API](https://frappe.io/api/method/frappe-library)


---

## 🧑‍💻 Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, Bootstrap 5
- **Database**: SQLite
- **API**: Frappe Book API

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/hassan962/Library_management_system.git
cd Library_management_system

# Create a virtual environment and activate it
python -m venv env
env\\Scripts\\activate  # Windows
source env/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver
