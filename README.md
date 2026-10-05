# Flask Market Simulation

A Flask-based market simulation and marketplace project built while learning Python web development, authentication, database-backed applications, and marketplace logic.

## Features

- Flask application factory pattern
- User authentication
- Account functionality
- Market and market-item functionality
- Database-backed application structure
- Flask-SQLAlchemy
- Flask-WTF and CSRF protection
- Modular Flask blueprints
- SQLite-oriented local development
- PostgreSQL-compatible configuration

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- SQLAlchemy
- Jinja2
- SQLite
- PostgreSQL

## Structure

~~~text
.
├── main.py
└── website/
    ├── init.py
    ├── auth.py
    ├── account.py
    ├── market.py
    ├── premium.py
    ├── model.py
    ├── views.py
    └── templates/
~~~

## Running Locally

~~~bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
~~~

## Learning Focus

This project helped me move from Python fundamentals toward full-stack development by combining routes, blueprints, forms, authentication, database models, and templates in one application.

## Status

Earlier version of the market-simulation project. The related marketsimulation repository contains the more developed version.