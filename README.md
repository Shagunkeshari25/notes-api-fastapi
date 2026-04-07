# Notes API with FastAPI

A secure and fully functional **Notes API** built with **FastAPI** and **SQLite**, allowing users to register, login, and manage their personal notes.

---

## Features

* **User Authentication**

  * Secure registration and login
  * Passwords hashed with **bcrypt**
  * JWT tokens for session management

* **Notes Management**

  * Create, Read, Update, Delete notes
  * Each user can access **only their own notes**
  * Pagination support with `limit` and `skip`

* **Data Validation & Error Handling**

  * Input validation using **Pydantic**
  * Proper error messages for unauthorized access and missing resources

---

## Technologies Used

* **Python 3.10+**
* **FastAPI** – Web framework
* **SQLAlchemy** – Database ORM
* **SQLite** – Database
* **Pydantic** – Data validation
* **Passlib** – Password hashing
* **Python-JOSE** – JWT authentication

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd notes-api-fastapi
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn Note.main:app --reload
```

* API URL: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc UI: http://127.0.0.1:8000/redoc

---

## API Endpoints

### User

* `POST /user/` – Create a new user
* `GET /user/{id}` – Get user details

### Authentication

* `POST /login` – Login and get JWT token

### Notes

* `GET /notes/` – Get all notes (with pagination)
* `POST /notes/` – Create a new note
* `GET /notes/{id}` – Get a specific note
* `PUT /notes/{id}` – Update a note
* `DELETE /notes/{id}` – Delete a note

---

## Usage

1. Create a user using `POST /user/`
2. Login using `POST /login`
3. Authorize in Swagger UI
4. Use Notes endpoints securely

---

## Notes

* JWT tokens expire in 30 minutes
* Users can only access their own notes
* API follows secure authentication and proper data handling

---

## Future Improvements

* Add search/filter for notes
* Add user roles (admin/user)
* Add password reset functionality

---
