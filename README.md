📒 Flask Notes App
A simple and intuitive Flask-based Notes Application that supports secure login, note creation, editing, and deletion.
 Built with Flask, SQLAlchemy, and SQLite, with a clean HTML/CSS interface.

📁 Project Structure
Your project structure (based exactly on your screenshot):
flask_app_notes-main/
│
├── __pycache__/              # Auto-generated Python cache files
│
├── instance/
│   └── app.db                # SQLite database (auto-created by Flask)
│
├── static/
│   └── style.css             # App styling
│
├── templates/
│   ├── edit.html             # Edit note page
│   ├── index.html            # Home listing + add notes
│   └── login.html            # Login page
│
├── venv/                     # Virtual environment (optional)
│
├── app.py                    # Main Flask application
├── data.py                   # Script to create users with hashed passwords
│
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation


🚀 Features
🔐 Authentication
Login protected routes


Passwords stored securely using hashing


User creation handled via data.py script


📝 Notes
Add a new note


Edit existing notes


Delete notes


View all notes in a clean, styled UI


🧱 Backend
SQLite database


SQLAlchemy ORM


login_required decorator for route protection


🎨 Frontend
Clean and minimal UI


Custom CSS styling



⚙️ Installation & Setup



1️⃣ Clone the repository
git clone <your-repo-url>
cd flask_app_notes-main

2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py

Your app is now live at:
http://127.0.0.1:5000/


👤 Adding Users (Hashed Passwords)

The login page does not include a signup form.
 
 Use the included data.py script to create users safely:
python data.py

You will be prompted for:

Enter new username: admin

Enter new password: ****

User 'admin' created successfully!


🌐 Route Overview

Route                  Method        Description          Login Required


/login                 GET/POST       Login screen            ❌


/logout                   GET          Ends session            ✔


/                         GET       Home page showing notes    ✔


/add                     POST          Add a new note          ✔


/edit/<id>              GET/POST         Edit note             ✔


/delete/<id>             GET            Delete note            ✔


🧠 Technologies Used  


Python 3


Flask


Flask-SQLAlchemy


Werkzeug Security


SQLite


HTML + CSS



📌 Recommended Improvements
Here are optional upgrades for your next version:
🔐 Security
Use check_password_hash() inside /login


Add CSRF protection (Flask-WTF)


Move secret_key to environment variable


👤 User System
Add signup page


Add per-user notes instead of shared global notes


🎨 UI/UX
Switch to Bootstrap or Tailwind


Add animations or icons


Add dark mode


📦 Features
Add note timestamps


Add categories/tags


Add search bar        




v
