# 🚗 VTravelBuddy - Full-Stack Ride Sharing App

[![Django](https://img.shields.io/badge/Django-4.2-blue)](#)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.4-38bdf8)](#)
[![Python](https://img.shields.io/badge/Python-3.11-yellow)](#)

**Live Demo:** https://vtravelbuddy.onrender.com

---

## ✨ Live Demo

🚀 **Production:** https://vtravelbuddy.onrender.com  
(Hosted on **Render** with persistent database.)

---

## 📸 Screenshots

- 📱 Mobile homepage  
- 🔎 Find ride  
- 🛠️ Admin panel  
- 🚗 Post ride  
- 💬 Chat option
- ![Home page](https://github.com/user-attachments/assets/0854f3cf-2937-4580-b3a0-411fcd931e7b)
![Find ride](https://github.com/user-attachments/assets/831934a3-e068-48ae-b545-fdaba380c365)
![Admin Panel](https://github.com/user-attachments/assets/3da417e6-ea5d-4204-a7bd-38faa620b8e5)
![Post ride](https://github.com/user-attachments/assets/9cb16856-2e52-4c47-9656-846d5f34f4ef)
![Chat Option](https://github.com/user-attachments/assets/94aafa8a-e6db-4eeb-b4ed-2f6baf76baa1)

> (Keep your existing `![...](...)` image links here.)

---

## 🧱 Tech Stack

| Frontend                      | Backend     | Database | Deployment | Styling          |
|------------------------------|------------|----------|------------|------------------|
| HTML5 + Django templates     | Django 4.2 | SQLite3  | Render     | Tailwind CSS 3.4 |

---

## 🚀 Quick Start (Local)

Clone repo
git clone https://github.com/YOURUSERNAME/vtravelbuddy.git
cd vtravelbuddy

Create virtual environment
python -m venv venv
venv\Scripts\activate # Windows

source venv/bin/activate # Mac/Linux
Install dependencies
pip install -r requirements.txt

Run migrations
python manage.py migrate

Create superuser
python manage.py createsuperuser

Start server
python manage.py runserver

- App: http://127.0.0.1:8000/  
- Admin: http://127.0.0.1:8000/admin/

---

## 🎯 Features

- ✅ Responsive design (Tailwind CSS, mobile-first)
- ✅ Ride creation, listing, and booking
- ✅ User authentication and profiles
- ✅ Admin dashboard for full management
- ✅ Production-ready static/media handling
- ✅ SEO-friendly server-side rendering

---

## 📁 Project Structure

vtravelbuddy/
├── backend/ # Django settings & URLs
├── travel/ # Main app (views, models, templates)
├── templates/ # HTML templates
├── static/ # CSS/JS (Tailwind)
├── media/ # User uploads
├── db.sqlite3 # Database
├── manage.py
└── README.md

---

## ⚙️ Deployment (Render)

1. Push your repo to GitHub.  
2. Create a new **Web Service** on Render and connect the repo.  
3. Set build command:  
   `pip install -r requirements.txt`  
4. Set start command:  
   `gunicorn backend.wsgi:application`  
5. Add environment variables as needed (e.g., `SECRET_KEY`, `DEBUG=0`).  
6. Run `python manage.py migrate` from Render shell after first deploy.

---

## 🎓 Learning Outcomes

- Django project setup & configuration  
- Tailwind CSS integration into Django  
- Database models, migrations, and admin panel  
- Static/media file pipelines  
- Production deployment on Render  
- Clean portfolio-ready full-stack project

---

## 👨‍💻 Author

**Layasri Pusapati** – B.Tech Computer Science, VIT Bhopal  
📧 layasripusapati@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/layasri-pusapati-2b773b250/)

---

## 📄 License

MIT License – feel free to use for learning and portfolio.
