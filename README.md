Smart Expense Tracker - Django project (skeleton)

This is a minimal, working Django project skeleton for the Smart Expense Tracker app.
It includes models, views, templates, static files and export endpoints (CSV/PDF placeholder).

How to run (in VS Code terminal):

1. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate   # mac/linux
   venv\Scripts\activate    # windows (powershell or cmd)

2. Install dependencies
   pip install -r requirements.txt

3. Run migrations
   python manage.py makemigrations
   python manage.py migrate

4. Create superuser (optional)
   python manage.py createsuperuser

5. Run server
   python manage.py runserver

Open http://127.0.0.1:8000/tracker/ in your browser.
Login page: http://127.0.0.1:8000/accounts/login/
Admin: http://127.0.0.1:8000/admin/
