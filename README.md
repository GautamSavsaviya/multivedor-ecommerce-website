# Django REST Framework and ReactJS Project

This project is a web application built using Django REST Framework (DRF) for the backend and ReactJS for the frontend. PostgreSQL is used as the database.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Backend](#backend)
  - [Django Setup](#django-setup)
  - [Database Configuration](#database-configuration)
  - [Running the Server](#running-the-server)
- [Frontend](#frontend)
  - [React Setup](#react-setup)
  - [Running the React App](#running-the-react-app)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your machine:
- Python (3.8 or later)
- Node.js (14.x or later)
- npm (6.x or later)
- PostgreSQL (12 or later)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

## Backend

### Django Setup

1. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

2. **Install the required Python packages:**
   ```sh
   pip install -r requirements.txt
   ```

### Database Configuration

1. **Configure PostgreSQL:**

   Ensure PostgreSQL is installed and running. Create a new database and user for the project.

   ```sql
   CREATE DATABASE your_db_name;
   CREATE USER your_db_user WITH PASSWORD 'your_db_password';
   ALTER ROLE your_db_user SET client_encoding TO 'utf8';
   ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE your_db_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
   ```

2. **Update `settings.py`:**

   In the Django project's `settings.py` file, update the `DATABASES` setting:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Running the Server

1. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

2. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```

3. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Frontend

### React Setup

1. **Navigate to the `frontend` directory:**
   ```sh
   cd frontend
   ```

2. **Install the required npm packages:**
   ```sh
   npm install
   ```

### Running the React App

1. **Start the React development server:**
   ```sh
   npm start
   ```

   The React app should now be running on [http://localhost:3000](http://localhost:3000).

## Built With

- [Django REST Framework](https://www.django-rest-framework.org/) - The web framework used for the backend
- [ReactJS](https://reactjs.org/) - The frontend library
- [PostgreSQL](https://www.postgresql.org/) - The database

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
