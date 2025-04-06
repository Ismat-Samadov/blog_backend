# Blog Backend API

A RESTful API backend for a blog application built with Django and Django REST Framework.

## Features

- **Post Management**: Create, read, update, and delete blog posts
- **Category System**: Organize posts by categories
- **User Authentication**: Secure API endpoints with user authentication
- **RESTful Interface**: Well-structured API following REST principles

## Tech Stack

- **Django 5.1.7**: High-level Python web framework
- **Django REST Framework 3.15.2**: Toolkit for building Web APIs
- **SQLite**: Database for development (can be configured for other databases)
- **Python 3**: Core programming language

## Project Structure

```
blog_backend/
├── api/                # API app
│   ├── serializers.py  # JSON serialization
│   ├── urls.py         # API endpoint routing
│   └── views.py        # API view logic
├── blog/               # Blog app
│   ├── admin.py        # Admin interface configuration
│   ├── models.py       # Database models
│   └── migrations/     # Database migrations
├── blog_project/       # Project settings
│   ├── settings.py     # Django configuration
│   ├── urls.py         # URL routing
│   └── wsgi.py         # WSGI configuration
├── manage.py           # Django command-line utility
├── requirements.txt    # Project dependencies
└── .env               # Environment variables (not tracked in git)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blog_backend.git
   cd blog_backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **API Root**: `/api/`
- **Posts**: `/api/posts/`
- **Categories**: `/api/categories/`
- **Authentication**: `/api/auth/`
- **Admin Panel**: `/admin/`

## Usage Examples

### List all posts
```
GET /api/posts/
```

### Get a specific post by slug
```
GET /api/posts/{slug}/
```

### Create a new post (authentication required)
```
POST /api/posts/
```
Request body:
```json
{
  "title": "My New Post",
  "slug": "my-new-post",
  "body": "Content of the post...",
  "category": 1,
  "status": "published"
}
```

### List all categories
```
GET /api/categories/
```

## Authentication

The API uses Django REST Framework's session authentication. To authenticate:

1. Visit `/api/auth/login/` and log in with your credentials
2. Make authenticated requests after logging in

## Development

### Running Tests
```bash
python manage.py test
```

### Creating New Migrations
```bash
python manage.py makemigrations
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
