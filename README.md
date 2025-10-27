# Diia Backend API

Backend API для iOS додатку Diia з інтеграцією Telegram бота.

## 🚀 Швидкий Деплой на Render

### ⚡ За 5 хвилин:
1. **[Швидкий чеклист →](QUICKSTART.md)** - Почати тут!
2. **[Детальна інструкція →](RENDER_DEPLOY.md)** - Всі кроки зі скріншотами

### Основні кроки:
```bash
# 1. Push на GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. На Render:
# - Створіть PostgreSQL database
# - Створіть Web Service
# - Додайте Environment Variables
# - Deploy!

# 3. Деталі дивіться в QUICKSTART.md
```

### Що вам потрібно:
- ✅ GitHub репозиторій
- ✅ Telegram Bot Token ([@BotFather](https://t.me/BotFather))
- ✅ Cloudinary Account ([cloudinary.com](https://cloudinary.com))
- ✅ Render Account ([render.com](https://render.com))

### Environment Variables:
```env
DATABASE_URL=postgresql://...  # З Render PostgreSQL
CLOUDINARY_URL=cloudinary://... # З Cloudinary Dashboard
BOT_TOKEN=...                    # З @BotFather
ADMIN_IDS=123456789             # Ваш Telegram ID
```

---

# Diia API Server

Backend API сервер для iOS приложения "Майже Дія" - авторизация, управление пользователями и подписками.

## Функционал

- 🔐 **Авторизация**: Login/Password authentication с bcrypt хешированием
- 👥 **Управление пользователями**: CRUD операции
- 💎 **Система подписок**: Управление подписками и их статусами
- 📸 **Cloudinary**: Загрузка и хранение фото пользователей
- 🗄️ **PostgreSQL/SQLite**: Поддержка обеих СУБД
- 📊 **Admin API**: Эндпоинты для администрирования

## Установка

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd DiiaAPI
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Настройка переменных окружения

Создайте файл `.env`:

```env
# Database URL
DATABASE_URL=postgresql://user:password@host:5432/database

# Cloudinary Settings
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name

# Admin IDs (for bot integration)
ADMIN_IDS=123456789

# Bot Token (for bot integration)
BOT_TOKEN=your_bot_token
```

### 4. Инициализация базы данных

База данных автоматически инициализируется при первом запуске.

## Запуск

### Локально (разработка)

#### FastAPI сервер (рекомендуется для разработки):

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

#### Flask сервер (для продакшена через Render):

```bash
gunicorn render_server:flask_app
```

или с указанием порта:

```bash
gunicorn -b 0.0.0.0:8000 render_server:flask_app
```

### На Render

Используйте `render_server.py` который совместим с Gunicorn.

```yaml
# render.yaml
services:
  - type: web
    name: diia-api
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn render_server:flask_app
    envVars:
      - key: DATABASE_URL
        value: your_postgresql_url
      - key: CLOUDINARY_URL
        value: your_cloudinary_url
```

## API Эндпоинты

### Авторизация

#### POST `/api/auth/login`

Авторизация пользователя

**Request:**
```json
{
  "login": "username",
  "password": "password"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Успішна авторизація",
  "user": {
    "id": 1,
    "full_name": "Іван Іванов",
    "birth_date": "01.01.2000",
    "login": "username",
    "subscription_active": true,
    "subscription_type": "premium",
    "last_login": "2025-10-27T00:00:00",
    "registered_at": "2025-10-20T00:00:00"
  }
}
```

### Пользователи

#### GET `/api/user/{login}`

Получить данные пользователя по логину

**Response:**
```json
{
  "full_name": "Іван Іванов",
  "birth_date": "01.01.2000",
  "photo_url": "https://cloudinary.com/...",
  "last_login": "2025-10-27T00:00:00",
  "subscription_active": true,
  "subscription_type": "premium",
  "subscription_until": "2025-11-27T00:00:00"
}
```

#### GET `/api/photo/{user_id}`

Получить фото пользователя (редирект на Cloudinary)

### Админ эндпоинты

#### GET `/api/admin/users`

Получить список всех пользователей

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "telegram_id": 123456789,
      "username": "user1",
      "full_name": "Іван Іванов",
      "birth_date": "01.01.2000",
      "photo_path": "https://cloudinary.com/...",
      "login": "user1",
      "subscription_active": true,
      "subscription_type": "premium",
      "subscription_until": "2025-11-27T00:00:00",
      "last_login": "2025-10-27T00:00:00",
      "registered_at": "2025-10-20T00:00:00",
      "updated_at": "2025-10-27T00:00:00"
    }
  ]
}
```

#### POST `/api/admin/grant-subscription`

Выдать подписку пользователю

**Request:**
```json
{
  "login": "username",
  "sub_type": "premium",
  "days": 30
}
```

**Response:**
```json
{
  "success": true,
  "message": "Підписку виданo користувачу Іван Іванов",
  "subscription_type": "premium",
  "subscription_until": "2025-11-27T00:00:00"
}
```

#### POST `/api/admin/update-subscription`

Обновить подписку пользователя

**Request:**
```json
{
  "user_id": 1,
  "active": true,
  "sub_type": "premium",
  "until": "2025-11-27T00:00:00"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Підписку оновлено"
}
```

### Health Check

#### GET `/api/health`

Проверка статуса сервера

**Response:**
```json
{
  "status": "ok",
  "message": "Server is running"
}
```

## Структура проекта

```
DiiaAPI/
├── api/
│   ├── __init__.py
│   ├── main.py          # FastAPI endpoints
│   └── admin.py         # Admin routes
├── database/
│   ├── __init__.py
│   └── models.py        # Database models
├── utils/
│   ├── __init__.py
│   └── cloudinary_helper.py
├── render_server.py     # Flask server for Render
├── requirements.txt     # Dependencies
├── README.md
└── .gitignore
```

## База данных

### Таблицы

**users** - Пользователи
- id, telegram_id, username, full_name, birth_date
- photo_path, login, password_hash
- subscription_active, subscription_type, subscription_until
- last_login, registered_at, updated_at

**sessions** - Сессии (для будущего использования)
- id, user_id, device_info, created_at

**registration_temp** - Временные данные регистрации (для бота)
- telegram_id, state, data, created_at

**payments** - Платежи (для бота)
- id, user_id, amount, currency, payment_method
- status, subscription_type, subscription_days
- created_at, completed_at

## Безопасность

- ✅ Пароли хешируются через `bcrypt`
- ✅ Использование PostgreSQL для продакшена
- ✅ Валидация всех входных данных
- ✅ CORS настроен для работы с iOS приложением
- ✅ Фото хранятся в Cloudinary (не на сервере)

## Интеграция с iOS приложением

### Авторизация

```swift
let loginData = ["login": "username", "password": "password"]
let url = URL(string: "https://your-api.com/api/auth/login")!

var request = URLRequest(url: url)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.httpBody = try? JSONSerialization.data(withJSONObject: loginData)

URLSession.shared.dataTask(with: request) { data, response, error in
    // Handle response
}.resume()
```

### Получение данных пользователя

```swift
let login = "username"
let url = URL(string: "https://your-api.com/api/user/\(login)")!

URLSession.shared.dataTask(with: url) { data, response, error in
    // Handle response
}.resume()
```

## Разработка

### Добавление новых эндпоинтов (FastAPI)

В `api/main.py`:

```python
@app.get("/api/my-endpoint")
async def my_endpoint():
    return {"message": "Hello"}
```

### Добавление новых эндпоинтов (Flask для Render)

В `render_server.py`:

```python
@flask_app.route("/api/my-endpoint", methods=["GET"])
def my_endpoint():
    return jsonify({"message": "Hello"})
```

## Troubleshooting

### Ошибки базы данных

1. Проверьте `DATABASE_URL` в `.env`
2. Убедитесь что PostgreSQL доступен
3. Проверьте права доступа к БД

### Ошибки Cloudinary

1. Проверьте `CLOUDINARY_URL`
2. Убедитесь в правильности API ключей
3. Проверьте квоту на Cloudinary

### Event loop errors

Если видите `Event loop is closed`:
- Убедитесь что используете правильный сервер (gunicorn для продакшена)
- Проверьте что `run_async()` функция работает корректно

## Деплой на Render

1. Создайте Web Service на Render
2. Подключите GitHub репозиторий
3. Настройте переменные окружения:
   - `DATABASE_URL`
   - `CLOUDINARY_URL`
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn render_server:flask_app`

## Мониторинг

### Логи

Логи доступны через:
- Render Dashboard (для production)
- Console output (для локальной разработки)

### Health Check

Проверить статус сервера:
```bash
curl https://your-api.com/api/health
```

## Поддержка

Если у вас возникли вопросы или проблемы, создайте issue в репозитории.

## Лицензия

MIT License

