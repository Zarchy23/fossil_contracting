# 🚀 Fossil Contracting - Production-Ready Full Stack

Complete Django + PostgreSQL backend with HTML/CSS/JS frontend for Zimbabwe's premier civil contracting company.

## 📋 Project Overview

**Tech Stack:**
- Backend: Django 4.2 + Django REST Framework
- Database: PostgreSQL
- Frontend: HTML5, CSS3, JavaScript (Vanilla)
- Server: Gunicorn (Production)

## 🗂️ Project Structure

```
fossil-contracting/
├── backend/                    # Django Application
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env                    # Environment variables
│   ├── fossil_backend/         # Main Django project
│   │   ├── __init__.py
│   │   ├── settings.py         # Django configuration
│   │   ├── urls.py             # URL routing
│   │   └── wsgi.py             # WSGI for production
│   └── api/                    # Django REST API
│       ├── models.py           # Database models
│       ├── views.py            # API views
│       ├── serializers.py      # DRF serializers
│       ├── urls.py             # API routes
│       ├── admin.py            # Django admin configuration
│       └── apps.py             # App configuration
│
├── frontend/                   # Static Frontend
│   ├── index.html              # Homepage
│   ├── about.html              # About page
│   ├── services.html           # Services page
│   ├── projects.html           # Projects page
│   ├── contact.html            # Contact page
│   ├── anonymous-feedback.html # Feedback page
│   ├── community-blog.html     # Blog page
│   ├── css/
│   │   └── style.css           # Main stylesheet
│   ├── js/
│   │   ├── api.js              # API client
│   │   └── main.js             # Main JavaScript
│   └── images/                 # Image assets
│
├── database/
│   └── init.sql                # Database initialization
│
└── README.md                   # This file
```

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip or conda

### Step 1: Install PostgreSQL & Create Database

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql

# In PostgreSQL interactive shell:
CREATE DATABASE fossil_db;
CREATE USER fossil_user WITH PASSWORD 'Fossil@2025Secure!';
ALTER ROLE fossil_user SET client_encoding TO 'utf8';
ALTER ROLE fossil_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE fossil_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE fossil_db TO fossil_user;
\quit
```

**Windows (using pgAdmin):**
1. Download and install PostgreSQL from https://www.postgresql.org/download/windows/
2. Open pgAdmin 4
3. Right-click "Databases" → Create → Database
4. Name: `fossil_db`
5. Create a new role `fossil_user` with password `Fossil@2025Secure!`
6. Grant all privileges to `fossil_user` on `fossil_db`

### Step 2: Setup Django Backend

```bash
# Navigate to project root
cd fossil-contracting

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Navigate to backend folder
cd backend

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations api
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
# Follow prompts to create username, email, and password
```

### Step 3: Load Initial Data (Optional)

```bash
# Option A: Using Django shell
python manage.py shell

from api.models import CompanyStat, Project

# Create statistics
CompanyStat.objects.create(label='Years Experience', value='25', icon='🏆', suffix='+', order=1)
CompanyStat.objects.create(label='Projects Completed', value='500', icon='📊', suffix='+', order=2)
CompanyStat.objects.create(label='ZBCA & CIFOZ', value='Category A', icon='⭐', order=3)
CompanyStat.objects.create(label='Safety Commitment', value='100%', icon='🛡️', order=4)

# Create sample project
Project.objects.create(
    name='Trabablas Interchange',
    location='Harare, Zimbabwe',
    value_usd=88.0,
    completion_percentage=85,
    client='Ministry of Transport',
    description='Construction of 15 bridges, Harare Drive Missing Link, Amalinda Road',
    status='ONGOING',
    is_featured=True,
    start_date='2023-01-01'
)

exit()
```

### Step 4: Run Backend Server

```bash
# Still in backend/ folder with virtual environment activated
python manage.py runserver

# Backend will be available at: http://localhost:8000
# Admin panel: http://localhost:8000/admin
# API endpoints: http://localhost:8000/api/
```

### Step 5: Serve Frontend

**Using Python's HTTP Server (Simple):**
```bash
# In a new terminal, navigate to frontend folder
cd frontend
python -m http.server 3000

# Frontend will be available at: http://localhost:3000
```

**Using Node.js (Alternative):**
```bash
# Install http-server globally
npm install -g http-server

# Serve frontend
cd frontend
http-server -p 3000
```

## 🔌 API Endpoints

### Feedback Management
- `GET /api/feedback/` - List all feedback
- `POST /api/feedback/` - Submit anonymous feedback

### Blog System
- `GET /api/blog/posts/` - List all blog posts
- `POST /api/blog/posts/` - Create new blog post
- `GET /api/blog/posts/<id>/` - Get specific post
- `PUT /api/blog/posts/<id>/` - Update post
- `DELETE /api/blog/posts/<id>/` - Delete post
- `POST /api/blog/posts/<id>/like/` - Like a post
- `GET /api/blog/posts/<post_id>/comments/` - Get comments
- `POST /api/blog/posts/<post_id>/comments/` - Add comment
- `POST /api/blog/comments/<id>/like/` - Like a comment

### Projects
- `GET /api/projects/` - Get all projects
- `GET /api/projects/featured/` - Get featured projects only

### Statistics
- `GET /api/stats/` - Get company statistics

## 🔐 Database Models

### 1. CompanyStat
- `label` - Name of statistic
- `value` - Value to display
- `icon` - Emoji icon
- `suffix` - Optional suffix (e.g., '+', '%')
- `order` - Display order

### 2. Feedback
- `type` - Type (COMPLAINT, SUGGESTION, PRAISE, INQUIRY)
- `message` - Feedback text
- `ip_hash` - Hashed IP for anonymity
- `is_read` - Read status
- `created_at` - Submission timestamp

### 3. BlogPost
- `title` - Post title
- `content` - Post content
- `author` - Author name (default: Anonymous)
- `view_count` - Number of views
- `like_count` - Number of likes
- `is_pinned` - Pin status
- `created_at` - Creation date
- `updated_at` - Last update date

### 4. BlogComment
- `post` - Foreign key to BlogPost
- `content` - Comment text
- `author` - Author name
- `like_count` - Number of likes
- `created_at` - Creation date

### 5. Project
- `name` - Project name
- `location` - Project location
- `value_usd` - Project value in USD
- `completion_percentage` - Progress percentage
- `client` - Client name
- `description` - Project description
- `status` - Status (PLANNING, ONGOING, COMPLETED, ON_HOLD)
- `image_url` - Image URL
- `is_featured` - Feature status
- `start_date` - Start date
- `end_date` - End date (nullable)
- `created_at` - Creation date

## 🔒 Admin Panel Access

1. Navigate to http://localhost:8000/admin
2. Login with superuser credentials created in Step 3
3. Manage:
   - Feedback submissions
   - Blog posts and comments
   - Projects
   - Statistics
   - User permissions

## 📊 Frontend Features

### Pages
- **Homepage** (`index.html`)
  - Hero section with call-to-action
  - Company statistics
  - Vision & Mission
  - Core values with circular promise design
  - Services overview
  - Anonymous features CTA
  - Footer

- **About** (`about.html`)
  - Company story
  - Team information
  - Company overview

- **Services** (`services.html`)
  - Complete list of services
  - Service descriptions
  - Links to contact

- **Projects** (`projects.html`)
  - All projects grid
  - Project details
  - Completion status
  - Project values

- **Contact** (`contact.html`)
  - Contact form
  - Office information
  - Hours of operation
  - Email and phone contact

- **Anonymous Feedback** (`anonymous-feedback.html`)
  - Anonymous feedback submission
  - No login required
  - IP hashing for privacy
  - Feedback list display

- **Community Blog** (`community-blog.html`)
  - Create blog posts
  - View community posts
  - Like posts
  - View comments

## 🎨 Styling

- **CSS Framework**: Custom CSS with modern design
- **Colors**: Green theme (primary: #166534)
- **Typography**: Inter font family
- **Responsive**: Mobile-first design with breakpoints at 768px and 1024px
- **Animations**: Smooth transitions and hover effects

## 🚀 Production Deployment

### Prepare for Production

```bash
# In backend folder
# Update settings.py
DEBUG = False
SECRET_KEY = "your-production-secret-key"
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Collect static files
python manage.py collectstatic --noinput

# Run server with gunicorn
gunicorn fossil_backend.wsgi:application --bind 0.0.0.0:8000
```

### Using Docker (Optional)

Create `Dockerfile` in project root:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
CMD ["gunicorn", "fossil_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Build and run:
```bash
docker build -t fossil-contracting .
docker run -p 8000:8000 fossil-contracting
```

## 📝 Environment Variables (.env)

```env
SECRET_KEY=your-secret-key-here
DEBUG=False              # Set to False in production
DB_NAME=fossil_db
DB_USER=fossil_user
DB_PASSWORD=Fossil@2025Secure!
DB_HOST=localhost
DB_PORT=5432
```

## 🔧 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000
# Kill the process
kill -9 <PID>
```

### PostgreSQL Connection Failed
```bash
# Check if PostgreSQL is running
sudo systemctl status postgresql

# Verify credentials in .env file
# Test connection
psql -U fossil_user -d fossil_db -h localhost
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## 📚 Additional Resources

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- PostgreSQL Documentation: https://www.postgresql.org/docs/

## ✅ Deployment Checklist

- [ ] Update SECRET_KEY in settings.py
- [ ] Set DEBUG=False
- [ ] Update ALLOWED_HOSTS
- [ ] Configure database credentials
- [ ] Run migrations on production database
- [ ] Collect static files
- [ ] Setup email configuration (if needed)
- [ ] Configure CORS for frontend domain
- [ ] Setup HTTPS/SSL certificate
- [ ] Configure backups
- [ ] Setup monitoring and logging

## 📞 Support

For issues or questions:
- Email: admin@fossilzim.com
- Phone: +263 8677 009771

## 📄 License

© 2025 Fossil Contracting. All rights reserved.
