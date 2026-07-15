# Django Shopping Cart Website

> A minimal Django e-commerce starter: product catalog, user auth, and the data model for a shopping cart.

## Overview

This is a small Django web application that lays down the backbone of an online store. It ships a product catalog rendered with Bootstrap, user registration and login built on Django's authentication system, and the relational models (`Product`, `Cart`, `CartItem`) needed to associate items with a user's cart. It's a compact, easy-to-read project — a good starting point for learning how a Django store fits together rather than a production storefront.

## Features

- **Product catalog** — products (name, price, description, image) are stored in the database and displayed as a responsive Bootstrap card grid on the store page.
- **User accounts** — registration, login, and logout built on Django's `UserCreationForm` and `AuthenticationForm`.
- **Cart data model** — `Cart` (one per user) and `CartItem` (product + quantity) with an `add-to-cart/<product_id>/` endpoint that creates or increments cart items.
- **Django admin** — the `Product` model is registered so you can add and manage catalog items through the built-in admin.
- **Media uploads** — product images are uploaded to `media/products/` and served in development.
- **Landing page** — a Bootstrap hero/landing page linking through to the store.

## Tech Stack

- **Framework:** Django 5.1
- **Language:** Python 3.10
- **Database:** SQLite (default `db.sqlite3`)
- **Frontend:** Django templates + Bootstrap 4.5 and Font Awesome (via CDN)

## Getting Started

```bash
# Clone the repository
git clone https://github.com/nickthelegend/django-shopping-cart-website.git
cd django-shopping-cart-website/shopping_cart

# (Recommended) create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate      # on Windows: myenv\Scripts\activate

# Install Django
pip install django

# Apply database migrations
python manage.py migrate

# Create an admin user to manage products
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` for the landing page, `http://127.0.0.1:8000/store/` for the catalog, and `http://127.0.0.1:8000/admin/` to add products.

> Note: the bundled `settings.py` uses `DEBUG = True` and a development secret key. Set a fresh `SECRET_KEY`, disable debug, and configure `ALLOWED_HOSTS` before deploying anywhere public.

## Project Structure

```
shopping_cart/
├── manage.py                 # Django management entry point
├── db.sqlite3                # SQLite database
├── media/                    # Uploaded product images
├── shopping_cart/            # Project configuration
│   ├── settings.py           # Settings (SQLite, installed apps, media)
│   ├── urls.py               # Root URL config (admin + store)
│   ├── wsgi.py / asgi.py     # Server entry points
│   └── __init__.py
└── store/                    # Main application
    ├── models.py             # Product, Cart, CartItem
    ├── views.py              # index, store, register, login, logout, add_to_cart
    ├── urls.py               # App routes
    ├── admin.py              # Product registered in admin
    ├── migrations/           # Database migrations
    └── templates/            # index, store, login, register
```

---

Built by [nickthelegend](https://github.com/nickthelegend) · [nickthelegend.tech](https://nickthelegend.tech)
