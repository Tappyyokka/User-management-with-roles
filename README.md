# 🚀 Flask User Management System (Deployed)

A full-stack Flask web application with authentication, role-based access control (RBAC), CRUD operations, REST APIs, and live cloud deployment.

🌐 **Live App:** https://user-management-with-roles.onrender.com

---

## ✨ Features

* 🔐 User Authentication (Login & Register)
* 🧑‍💼 Role-Based Access Control (Admin / User)
* 📊 Student Management (CRUD operations)
* 🌐 REST API with JSON responses
* 🎨 Clean modern UI with profile dropdown
* ☁️ Deployed on cloud (Render)

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Authentication:** Flask Sessions + Werkzeug
* **Deployment:** Render
* **Server:** Gunicorn

---

## 📂 Project Structure

```
project/
│── app.py
│── database.db
│── requirements.txt
│── Procfile
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── students.html
│   ├── add_student.html
│   └── edit_student.html
│
├── static/
│   └── style.css
```

---

## ⚙️ Deployment (Render)

Steps followed:

1. Disabled debug mode
2. Used environment variable for secret key
3. Created `requirements.txt`
4. Added `Procfile` → `web: gunicorn app:app`
5. Pushed code to GitHub
6. Connected repo to Render
7. Deployed successfully 🎉

---

## 🔒 Security

* Password hashing (Werkzeug)
* Session-based authentication
* Role-based route protection
* No plain-text passwords

---

## 🧪 API Endpoints

| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| GET    | /api/students      | Get all students |
| POST   | /api/students      | Add student      |
| PUT    | /api/students/<id> | Update student   |
| DELETE | /api/students/<id> | Delete student   |

---

## 🚀 Future Improvements

* Search & pagination
* Better UI animations
* Profile settings page
* PostgreSQL integration

---

## 👨‍💻 Author

**Abhinand M**

---

## ⭐ Internship Project

Built as part of a Full Stack Web Development Internship, progressing from basic Flask apps to a fully deployed production-ready system.
