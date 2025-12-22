🚗 VTravelBuddy - Full-Stack Ride Sharing App
[![Django](https://github.com/layasri157/vtravelbuddy/actions/workflows/ci.yml/badge.svg)](https://github.com/layasri157/vtravelbuddy/actions)

[![Django](https://img.shields.io/badge/Django-4.2-blue![TailwindCSS](https://img.shields.io/badge/TailwindCSS-![Python](https://img.shields.io/badge/Python-3.11-yellowLive Demo: https://your-vtravelbuddy.herokuapp.com (Update after deployment)

## ✨ **Live Demo** 
🚀 **[https://vtravelbuddy.onrender.com](https://vtravelbuddy.onrender.com)**


✨ Screenshots
📱 Mobile Homepage
![Home page](https://github.com/user-attachments/assets/0854f3cf-2937-4580-b3a0-411fcd931e7b)
![Find ride](https://github.com/user-attachments/assets/831934a3-e068-48ae-b545-fdaba380c365)
![Admin Panel](https://github.com/user-attachments/assets/3da417e6-ea5d-4204-a7bd-38faa620b8e5)
![Post ride](https://github.com/user-attachments/assets/9cb16856-2e52-4c47-9656-846d5f34f4ef)
![Chat Option](https://github.com/user-attachments/assets/94aafa8a-e6db-4eeb-b4ed-2f6baf76baa1)




Frontend	Backend	Database	Deployment	Styling
HTML5 + Django Templates	Django 4.2	SQLite3	Heroku/Railway	Tailwind CSS 3.4
🚀 Quick Start (Local)
bash
# Clone repo
git clone https://github.com/YOURUSERNAME/vtravelbuddy.git
cd vtravelbuddy

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install django==4.2

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
Visit: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

🎯 Features
✅ Responsive Design - Mobile-first Tailwind CSS

✅ Admin Dashboard - Full user management

✅ Production Ready - Static/media files configured

✅ Clean Architecture - Django best practices

✅ Fast Loading - Optimized templates

✅ SEO Friendly - Server-side rendering

📁 Project Structure
vtravelbuddy/
├── backend/           # Django settings & URLs
├── travel/            # Main app (views, models, templates)
├── templates/         # HTML templates
├── static/            # CSS/JS (Tailwind)
├── media/             # User uploads
├── db.sqlite3         # Database
├── manage.py
└── README.md
⚙️ Deployment Guide
Heroku (Recommended)
bash
# 1. Install Heroku CLI
# 2. Login
heroku login

# 3. Create app
heroku create your-vtravelbuddy-app

# 4. Deploy
git push heroku main
heroku run python manage.py migrate
heroku open
Railway (Free Alternative)
Connect GitHub repo to railway.app

Deploy automatically ✅

🎓 Learning Outcomes
Django project setup & configuration

Tailwind CSS integration

Database migrations & admin panel

Static/media file handling

Production deployment

GitHub portfolio project

👨‍💻 Author
Layasri Pusapati
VIT Bhopal - B.Tech Computer Science
📧 layasripusapati@gmail.com
💼 LinkedIn: (https://www.linkedin.com/in/layasri-pusapati-2b773b250/)

📄 License
MIT License - Feel free to use for learning/portfolio!
