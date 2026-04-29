# Hospital Management System

A Flask-based Hospital Management System for managing patients, doctors, appointments, medical records, billing, users, notifications, and a simple hospital help chatbot.

## Features

- Patient registration and profile management
- Doctor profile management with specialization and availability data
- Appointment scheduling, editing, cancellation, and status tracking
- Medical record management for patient treatment history
- Billing records with payment status tracking
- Role-based access for administrators, doctors, staff, and patients
- Admin user management

## Project Structure

```text
hospital-management-system/
|-- app/
|   |-- __init__.py
|   |-- routes/
|   |-- models/
|   |-- templates/
|   `-- static/
|-- database/
|   |-- create_admin.sql
|   `-- hospital_system.sql
|-- scripts/
|   |-- create_admin.py
|   `-- update_schema.py
|-- run.py
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create the MySQL database:

```bash
mysql -u root -p < database/hospital_system.sql
```

4. Configure environment variables in a local `.env` file:

```env
SESSION_SECRET=change-this-secret
MYSQL_USER=root
MYSQL_PASSWORD=your-password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=hospital_system
```

5. Create or update the default admin user:

```bash
python scripts/create_admin.py
```

By default, the admin credentials are `admin` / `admin123`. Override them with `ADMIN_USERNAME`, `ADMIN_EMAIL`, and `ADMIN_PASSWORD` environment variables.

## Run

```bash
python run.py
```

Open `http://localhost:5000` in your browser.
