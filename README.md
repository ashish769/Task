# Django RBAC API Project

This project implements a **Role-Based Access Control (RBAC) API** using **Django** and **Django REST Framework (DRF)**. Users are assigned roles (**ADMIN, AUTHOR, READER**), and access to API endpoints is restricted based on these roles. Authentication uses **JWT (JSON Web Tokens)**.

---

## Table of Contents

- [Setup Instructions](#setup-instructions)  
- [Required Environment Variables](#required-environment-variables)  
- [API Endpoints](#api-endpoints)  
- [Sample Requests & Responses](#sample-requests--responses)  
- [Dependencies](#dependencies)  

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/ashish769/Task.git
cd Task

```
2. **Create a virtual environment**

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5.**Run the development server**
```bash
python manage.py runserver
```

# Required Environment Variables

Create a .env file in the project root and include:
```bash
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

## Make user from the CLI
```bash
python manage.py create_user --username reader1 --password 1234 --role READER

```
## API Endpoints

The following table lists all available API endpoints, their functionality, and the roles allowed to access them.

| Method | Endpoint               | Description                     | Access Role                                 |
|--------|-----------------------|---------------------------------|--------------------------------------------|
| POST   | `/api/token/`         | Obtain JWT access and refresh   | All                                        |
| POST   | `/api/token/refresh/` | Refresh access token            | All                                        |
| GET    | `/api/blogs/`         | List all blogs                  | All Authenticated Users (including READER)|
| GET    | `/api/blogs/<id>/`    | Retrieve a specific blog        | All Authenticated Users (including READER)|
| POST   | `/api/blogs/`         | Create a new blog               | AUTHOR / ADMIN                             |
| PUT    | `/api/blogs/<id>/`    | Update a blog                   | AUTHOR (own blogs) / ADMIN                 |
| DELETE | `/api/blogs/<id>/`    | Delete a blog                   | ADMIN                                      |

> **Note for Readers:**  
> Readers are authenticated users with the **READER** role.  
> They can only access `GET /api/blogs/` and `GET /api/blogs/<id>/` to read blogs. All other operations are restricted to **AUTHOR** or **ADMIN** roles.


# Sample Requests & Responses

### 1. Obtain JWT Token

**Request:**

```bash
POST /api/token/
Content-Type: application/json

{
  "username": "author1",
  "password": "1234"
}
```

**Response:**
```bash

{
  "access": "eyJ0eXAiOiJKV1QiLCJh...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJh..."
}
```
