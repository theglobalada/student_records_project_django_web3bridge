# My Student Records Project

This repository contains the Django application I built for keeping track of student information.  I started it as part of my coursework to practise working with models, views and templates in Django.  The app lets me add students, view their details, update entries and delete records when needed.  

I kept the interface simple on purpose so I could focus on the backend logic and understand how Django's admin panel works.  There are only two main pages: a list of all students and a form to create/edit a student.  

**How I used it**

1. I created a Python virtual environment and installed Django.
2. I ran `python manage.py makemigrations` and `python manage.py migrate` to set up the database.
3. I started the server with `python manage.py runserver` and opened `http://127.0.0.1:8000/students/` in my browser.
4. For admin access I used the superuser account I created during development.

---
