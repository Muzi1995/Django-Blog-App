GradVoyage

A modern Django web application where users can register, log in, and create posts with images.
This project was built step by step while learning Django — covering everything from environment setup to authentication, authorization, ORM, and custom forms.

✨ Features

🔐 User Authentication & Authorization

Register, log in, log out

Restrict certain pages to logged-in users only

📰 Posts Management

List all posts

Individual post detail pages with clean slugs

Create new posts (title, body, slug, image, author)

🖼 Image Uploads

Upload and display post banners

Default fallback image support

🎨 Modern UI

Responsive layout with custom CSS styling

Navigation bar with icons + project branding

Includes logo and favicon

⚙️ Django Admin

Manage posts via Django’s built-in admin dashboard

🛠 Database Integration

Fully powered by Django ORM (Object-Relational Mapper)

SQLite by default, extendable to PostgreSQL/MySQL

🛠 Tech Stack

Backend: Python, Django

Frontend: HTML5, CSS3, Django Template Language

Database: SQLite (default)

Auth System: Django auth


myproject/

│── manage.py

│── myproject/

│    ├── settings.py

│    ├── urls.py

│    └── ...

│── posts/

│    ├── models.py

│    ├── views.py

│    ├── urls.py

│    ├── forms.py

│    └── templates/posts/

│── users/

│    ├── views.py

│    ├── urls.py

│    └── templates/users/

│── templates/

│    └── layout.html

│── static/

│    ├── css/style.css

│    ├── js/main.js

│    └── img/GradVoyage.png

│── media/ (uploaded images)


📦 Key Commands Used:

Command	Purpose

python -m venv .venv	Create virtual environment

.venv\Scripts\activate / source .venv/bin/activate	Activate venv

pip install Django Pillow	Install dependencies

django-admin startproject myproject .	Create new Django project

python manage.py startapp posts	Create new app

python manage.py makemigrations	Generate DB migrations

python manage.py migrate	Apply migrations

python manage.py runserver	Start dev server

python manage.py shell	Interactive Python shell

python manage.py createsuperuser	Create admin user

python manage.py collectstatic	Collect static files for production



🛡 Troubleshooting

CSRF verification failed → Add {% csrf_token %} inside all <form method="post">.

NoReverseMatch → Ensure {% url 'app:view' %} matches urls.py names exactly.

Slug errors (empty slug) → Check via python manage.py shell and update:

from posts.models import Post

from django.utils.text import slugify

p = Post.objects.get(id=1)

p.slug = slugify(p.title)

p.save()


Image not showing → Ensure MEDIA_URL, MEDIA_ROOT are configured and urlpatterns += static(...) is present.

Static/Media missing in production → Run python manage.py collectstatic.

📖 What I Learned

How to set up a Django project from scratch.

Understanding URLs, Views, Templates (MVT).

Managing models, migrations, and queries with Django ORM.

Implementing user authentication & authorization.

Handling static files and media uploads.

Creating custom forms and associating posts with authors.

Using Django Admin for content management.

Styling and branding with CSS, logos, and favicon.

Media Handling: Django ImageField, Pillow

Other Tools: Virtual environment (venv), collectstatic, CSRF protection



📜 License

This project is for learning purposes. Feel free to fork and extend.

🔥 Proudly built while learning Django → GradVoyage 🎓✈️



