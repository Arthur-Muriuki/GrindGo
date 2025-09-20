GrindGo

Work hard. Go far. Grind smart.

A lightweight Django-based app for managing routines and daily grind. GrindGo helps you organize habits, tasks, and routines so that you’re always leveling up.

🎯 Table of Contents

Features

Tech Stack

Setup & Installation

Usage

Project Structure

Contributing

License

Features

Manage daily routines / habits

Track progress over time

Simple, clean UI for entering tasks

Lightweight & minimal dependencies

(Potential) User authentication & permissions

(Potential) Analytics / dashboard showing your streaks

Tech Stack
Component	Technology
Backend	Django (Python)
Database	SQLite (default)
Frontend	Django templates + HTML/CSS
Version Control	Git / GitHub
Setup & Installation

Here’s how you get GrindGo running locally.

Clone the repo

git clone https://github.com/Arthur-Muriuki/GrindGo.git
cd GrindGo


Create a virtual environment

python3 -m venv venv
source venv/bin/activate  # on Unix/macOS
# or
venv\Scripts\activate     # on Windows


Install dependencies

pip install -r requirements.txt


Database setup / migrations

python manage.py migrate


Run development server

python manage.py runserver


Open in browser
Navigate to http://127.0.0.1:8000/ (or whatever host:port it shows).

Usage

Create / edit routines or tasks

View routine schedule

Mark tasks complete / track progress

(Future) Authenticate users, view dashboards

Project Structure
GrindGo/
├── Grindgo/           # main app folder (models, views, templates)
├── Routineapp/        # maybe for routines/tasks logic
├── db.sqlite3         # default dev database
├── manage.py
└── requirements.txt


Grindgo/ — core app: templates, static files, URLs, etc.

Routineapp/ — the module for routines / tasks logic.

db.sqlite3 — default local DB; can be swapped for Postgres/MySQL in production.

Contributing

Cool that you’re thinking of helping!

Fork the repo

Create a feature branch (git checkout -b feature/some-feature)

Write tests if possible

Open a Pull Request and include a description of changes

Be kind. Reviewers are people too 🧑‍💻

Roadmap (Future ideas)

User authentication / registration

Dashboard with charts (streaks etc.)

Notifications / reminders

Mobile-responsiveness

Export / sync data

License
