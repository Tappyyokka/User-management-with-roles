# 🚀 Student Management System (Flask + RBAC + REST API)

This project is a **Student Management System** built using **Flask** and **SQLite**, upgraded to a **production-style backend system** as part of my internship (Task 4).

It includes **role-based access control (RBAC)**, **admin/user separation**, and **REST API endpoints** for managing data.

---

## ✨ Features

### 🔐 Authentication

* User Registration & Login
* Password hashing (Werkzeug)
* Session-based authentication

### 👑 Role-Based Access Control (RBAC)

* Two roles: **Admin** and **User**
* Admin → full access
* User → read-only access
* Protected routes using decorators

### 📊 Dashboard

* Personalized dashboard
* Total students count
* Quick navigation (SaaS-style UI)

### 📋 Student Management (CRUD)

* ➕ Add Students *(Admin only)*
* 📄 View Students *(All users)*
* ✏️ Edit Students *(Admin only)*
* 🗑️ Delete Students *(Admin only)*

### 👑 Admin Panel

* View all users
* Role visibility (Admin/User)

---

## 🌐 REST API

### Endpoints:

| Method | Endpoint             | Access          | Description      |
| ------ | -------------------- | --------------- | ---------------- |
| GET    | `/api/students`      | Logged-in users | Get all students |
| POST   | `/api/students`      | Admin only      | Add student      |
| PUT    | `/api/students/<id>` | Admin only      | Update student   |
| DELETE | `/api/students/<id>` | Admin only      | Delete student   |

---

## 🔐 Security Features

* Route protection using session-based authentication
* Admin-only API access for write operations
* Unauthorized access returns proper HTTP status codes
* Passwords stored securely using hashing

---

## 🛠️ Tech Stack

* Python 🐍
* Flask 🌐
* SQLite 🗄️
* HTML & CSS 🎨

---

## 📁 Project Structure

```
project/
│
├── app.py
├── database.db (ignored in git)
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── students.html
│   ├── add_student.html
│   ├── edit_student.html
│   └── admin.html
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── dashboard.png
│   ├── students.png
│   ├── admin.png
│   ├── api-get.png
│   ├── api-post.png
│   └── api-security.png
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
```

2. Navigate into project:

```
cd your-repo
```

3. Install dependencies:

```
pip install flask
```

4. Run the app:

```
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### 🏠 Dashboard

![Dashboard](screenshots/dashboard.png)

### 📋 Students Page

![Students](screenshots/students.png)

### 👑 Admin Panel

![Admin](screenshots/admin.png)

### 🌐 API Testing (GET)

![API GET](screenshots/api-get.png)

### ➕ API Testing (POST)

![API POST](screenshots/api-post.png)

### 🔐 API Security (User Blocked)

![API Security](screenshots/api-security.png)

---

## 🧪 API Testing

API endpoints were tested using:

* Postman
* Thunder Client (VS Code)

---

## 📚 What I Learned

* Implementing RBAC (Role-Based Access Control)
* Securing backend routes and APIs
* Designing RESTful APIs
* Managing sessions in Flask
* Connecting frontend UI with backend logic

---

## 🚀 Future Improvements

* 🔍 Search & filter students
* 📊 Dashboard analytics
* 📱 Mobile responsive UI
* 🌙 Dark mode
* 👥 Role management (change roles from admin panel)

---

## 🙌 Acknowledgment

This project was built as part of my internship learning journey.

---

## 📬 Connect with me

Feel free to connect or share feedback!
