# Employee Feedback System

A web-based Employee Feedback Management System built with **Django** that allows organizations to collect and manage employee information and feedback through a structured form interface. The application stores data in a **Microsoft SQL Server database running inside a Docker container**, providing a realistic production-style backend setup.

---

## Overview

This project demonstrates a complete backend workflow using Django, including form validation, ORM-based database operations, and an administrative dashboard for managing records.

Users can submit employee feedback through a responsive form interface. The backend validates the data, persists it in SQL Server, and allows administrators to manage records through Django's built-in admin panel.

---

## Features

* Employee feedback submission form
* Server-side validation using Django Forms
* Data storage using Microsoft SQL Server
* SQL Server containerized with Docker
* Django ORM for database operations
* Admin dashboard for CRUD operations
* Responsive form UI using Bootstrap
* Custom validation rules (e.g., phone number format, employee ID format)

---

## Tech Stack

**Backend**

* Python
* Django
* Django ORM

**Database**

* Microsoft SQL Server
* Docker (containerized SQL Server instance)
* ODBC Driver 18 for SQL Server
* pyodbc
* mssql-django

**Frontend**

* HTML
* Bootstrap

**Development Tools**

* VS Code
* Git & GitHub
* Docker

---

## System Architecture

User interaction follows the workflow below:

User Browser
→ Django Template (HTML Form)
→ Django View
→ Django Form Validation
→ Django ORM
→ SQL Server Database (Docker container)

---

## Project Structure

```
employee-feedback-system
│
├── employee_project/
│   │
│   ├── employee_project/        # Django project configuration
│   │     ├── settings.py
│   │     ├── urls.py
│   │     ├── asgi.py
│   │     └── wsgi.py
│   │
│   ├── employees/               # Django application
│   │     ├── migrations/
│   │     ├── templates/
│   │     │     └── employees/
│   │     │           ├── employee_form.html
│   │     │           └── success.html
│   │     │
│   │     ├── models.py
│   │     ├── views.py
│   │     ├── forms.py
│   │     ├── urls.py
│   │     ├── admin.py
│   │     └── apps.py
│   │
│   └── manage.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/sumedhp23/employee-feedback-system.git
cd employee-feedback-system
```

---

### 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Start SQL Server using Docker

```
docker run -e "ACCEPT_EULA=Y" \
-e "SA_PASSWORD=YourStrongPassword!" \
-p 1433:1433 \
--name sql_server_container \
-d mcr.microsoft.com/mssql/server:2025-latest
```

---

### 5. Create the database

Access the SQL Server container:

```
docker exec -it sql_server_container /opt/mssql-tools18/bin/sqlcmd \
-S localhost -U SA -P "YourStrongPassword!" -C
```

Create the database:

```
CREATE DATABASE employee_db;
GO
```

---

### 6. Run migrations

```
python manage.py migrate
```

---

### 7. Create an admin user

```
python manage.py createsuperuser
```

---

### 8. Start the development server

```
python manage.py runserver
```

Open the application:

```
http://127.0.0.1:8000
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

## Database Design

The primary table created by Django is:

```
employees_employeefeedback
```

It stores:

* Employee Name
* Employee ID
* Department
* Email
* Phone Number
* Joining Date
* Experience
* Feedback
* Recommendations

---

## Future Improvements

Potential enhancements for this system:

* Employee dashboard with record listing
* Edit and delete employee records through UI
* REST API using Django REST Framework
* Authentication and role-based access
* Search and filtering functionality
* Deployment using Docker Compose

---

## Author

Sumedh Patil

---

## License

This project is intended for educational and portfolio purposes.
