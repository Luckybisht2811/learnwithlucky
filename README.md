# 🎓 LearnWithLucky — Full-Stack Django E-Learning Platform

**A modern online learning platform for courses and notes with a clean UI and smart features.**

🔗 **Live Demo:** *(Add your deployed link here)*

---

## 📌 Overview

**LearnWithLucky** is a full-stack **E-Learning Web Application** built with **Django, Python, Tailwind CSS/HTML/JS**.
It allows users to explore courses, access notes, and learn efficiently through a modern and responsive interface.

This project demonstrates **full-stack development, UI design, search functionality, and authentication system** — making it a strong portfolio project.

---

## 🚀 Features

### 💻 User Features

* User registration & secure login
* Browse multiple courses
* Access structured notes
* Smart search functionality (courses + notes)
* Responsive design (mobile + desktop)
* Clean and modern UI

### ⚙️ Admin Features

* Upload courses and notes
* Manage learning content
* Update and organize study materials

### 🛠 Technical Features

* Backend: **Django (Python)**
* Frontend: **HTML5, Tailwind CSS, JavaScript**
* Database: **SQLite**
* Authentication system
* JSON-based dynamic search
* Responsive UI design

---

## 📂 Project Structure

```text
LMS Portal/
│
├─ course/              # Main Django app
│  ├─ migrations/
│  ├─ static/course/    # CSS, JS, Images
│  ├─ templates/course/ # HTML templates
│  ├─ models.py
│  ├─ views.py
│  └─ urls.py
│
├─ lms/                 # Project settings
├─ manage.py
├─ db.sqlite3
├─ requirements.txt
└─ .gitignore
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Luckybisht2811/learnwithlucky.git
cd learnwithlucky
```

### 2️⃣ Create virtual environment

```bash
python -m venv env
env\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the server

```bash
python manage.py runserver
```

👉 Open in browser: http://127.0.0.1:8000/

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

---

## 📸 Screenshots

> (Add screenshots of your homepage, courses page, notes page, etc.)

---

## 🚀 Future Improvements

* 🎥 Video course upload system
* 💳 Payment integration
* 📊 User dashboard
* 🔔 Notifications system
* 📱 Mobile app version

---

## 👨‍💻 Author

**Lucky (Lalit Singh Bisht)**

* GitHub: https://github.com/Luckybisht2811

---

## 📝 License

This project is open-source and free for learning & portfolio purposes.

---

## ⭐ Show Your Support

If you like this project, please ⭐ star the repository and share it!
