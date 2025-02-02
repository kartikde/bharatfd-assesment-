

## Project Overview
This project implements a Django-based FAQ system with the following features:
- WYSIWYG editor for rich-text answers using `django-ckeditor`
- Multilingual FAQ storage with Google Translate integration
- REST API for managing FAQs with language selection
- Caching using Redis for optimized performance
- Admin panel for FAQ management
- Unit tests for model methods and API responses
- PEP8 compliance and Git best practices

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Redis (for caching)
- Git (for version control)

### Step 1: Clone the Repository
```sh
git clone <your-repo-link>
cd faq_project
```

### Step 2: Set Up Virtual Environment
```sh
python -m venv venv
venv\Scripts\activate  # On Windows
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Configure Redis (Windows)
Ensure Redis is running locally on `127.0.0.1:6379`.

### Step 5: Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser
```sh
python manage.py createsuperuser
```

### Step 7: Run the Server
```sh
python manage.py runserver
```
Access the Admin Panel at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## API Endpoints
### Fetch FAQs (Default: English)
```sh
GET /api/faqs/
```

### Fetch FAQs in Hindi
```sh
GET /api/faqs/?lang=hi
```

### Fetch FAQs in Bengali
```sh
GET /api/faqs/?lang=bn
```

## Testing
Run unit tests using:
```sh
pytest
```

