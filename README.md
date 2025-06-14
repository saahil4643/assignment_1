# Django REST API with Celery, Redis & Telegram Bot Integration

A full-stack Django application using Django Rest Framework, JWT Auth, Celery, Redis, and Telegram Bot API.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/django-telegram-bot.git
cd django-telegram-bot
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file in the project root:

```ini
# .env

SECRET_KEY=your_django_secret_key
DEBUG=False

# Email settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.yourmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=yourpassword

# Redis settings
REDIS_URL=redis://localhost:6379/0

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

---

## ▶️ Run Locally

### Run Django Server

```bash
python manage.py runserver
```

### Start Redis Server

Make sure Redis is installed and running:

```bash
redis-server
```

### Start Celery Worker

```bash
celery -A myproject worker --pool=solo --loglevel=info
```

### Start Telegram Bot

```bash
python manage.py run_telegram_bot
```

---

## 🌐 API Documentation

### 🔑 JWT Authentication

#### Obtain Token
`POST /api/token/`

**Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

#### Refresh Token
`POST /api/token/refresh/`

**Body:**
```json
{
  "refresh": "your_refresh_token"
}
```

### 🧾 Endpoints Summary

| Endpoint                       | Access       | Method | Description                           |
|--------------------------------|--------------|--------|---------------------------------------|
| `/api/messages/public/`        | Public       | GET    | Publicly accessible messages          |
| `/api/messages/protected/`     | JWT Required | GET    | Messages for authenticated users only |
| `/register/`                   | Public       | POST   | User registration with email          |
| `/login/`                      | Public       | POST   | Web login page                        |
| `/dashboard/`                  | Auth Required| GET    | User dashboard page                   |

---

## 📩 Celery + Redis Setup

- Background task `send_welcome_email` runs after user registration.
- Uses Celery for task queuing.
- Redis as the message broker.

### Task Execution Flow

1. User registers via `/register/`
2. Celery task `send_welcome_email` is queued
3. Redis broker passes the task to the worker
4. Email is sent asynchronously

---

## 💬 Telegram Bot Integration

### Features
- Responds to `/start` command
- Collects Telegram user data and saves it to Django DB

### Setup

1. Go to [@BotFather](https://t.me/BotFather)
2. Create a bot and get your bot token
3. Add the token in `.env` as `TELEGRAM_BOT_TOKEN`
4. Run:
```bash
python manage.py run_telegram_bot
```

---

## 📁 Project Structure

```
myproject/
│
├── myproject/                 # Project config
│   ├── settings.py
│   └── urls.py
│
├── myapp/                     # Main application
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── tasks.py               # Celery tasks
│   ├── templates/             # login.html, register.html
│   └── management/commands/   # run_telegram_bot.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 📦 requirements.txt (sample)

```txt
Django>=4.2
djangorestframework
djangorestframework-simplejwt
python-dotenv
celery
redis
python-telegram-bot==13.15
```

---

## 🧪 Test Your Setup

- Access: `http://127.0.0.1:8000/`
- Test `/api/messages/public/`
- Use Postman to obtain token and hit `/api/messages/protected/`
- Register a user on `/register/` → Email gets sent
- Send `/start` to your bot → User data saved in DB

---

## 📘 Tech Stack

- Django
- Django Rest Framework
- JWT Authentication
- Celery
- Redis
- Telegram Bot API
- PostgreSQL / SQLite (choose your DB)

---

## 📄 License

MIT License

---

## ✍️ Author

Built by [Your Name](https://github.com/YOUR_USERNAME) 💻

Feel free to fork, star ⭐ and contribute!