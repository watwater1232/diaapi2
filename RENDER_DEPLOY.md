# 🚀 Деплой на Render - Детальна Інструкція

## Крок 1: Підготовка

### 1.1 Перевірте, що є в репозиторії:
- ✅ `Procfile` - для запуску додатку
- ✅ `requirements.txt` - залежності
- ✅ `render.yaml` - конфігурація (опціонально)
- ✅ `.env` файл НЕ комітиться (додайте в `.gitignore`)

### 1.2 Push на GitHub:
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

## Крок 2: Створення Database на Render

1. Зайдіть на [Render Dashboard](https://dashboard.render.com)
2. Натисніть **"New +"** → **"PostgreSQL"**
3. Введіть ім'я: `diia-db`
4. Виберіть **"Free"** план
5. Оберіть регіон (найближчий до вас)
6. Натисніть **"Create Database"**
7. **Скопіюйте Internal Database URL** - він починається з `postgresql://`
8. Збережіть його - він буде використовуватись як `DATABASE_URL`

## Крок 3: Створення Web Service

1. Натисніть **"New +"** → **"Web Service"**
2. Підключіть ваш GitHub репозиторій
3. Введіть налаштування:
   - **Name:** `diia-api` (або як вам подобається)
   - **Runtime:** `Python 3`
   - **Region:** той самий, що й для database
   - **Branch:** `main` (або ваша гілка)
   - **Root Directory:** `.` (залиште порожнім)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py flask`
4. Натисніть **"Advanced"** і додайте Environment Variables:

### Environment Variables:

```bash
# Database
DATABASE_URL=<вставте Internal Database URL з кроку 2>

# Cloudinary (створіть аккаунт на cloudinary.com)
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name

# Telegram Bot (отримайте від @BotFather)
BOT_TOKEN=your_bot_token_here

# Admin IDs (ваші Telegram ID, розділені комою)
ADMIN_IDS=123456789,987654321

# CryptoPay (опціонально)
CRYPTOPAY_TOKEN=your_cryptopay_token

# Python Version
PYTHON_VERSION=3.11.0
```

5. Виберіть **"Free"** план
6. Натисніть **"Create Web Service"**

## Крок 4: Чекайте деплой

Render буде:
1. Клонувати ваш репозиторій
2. Встановлювати залежності
3. Запускати ваш додаток

Це займе ~5-10 хвилин вперше.

## Крок 5: Налаштування Telegram Webhook

Після успішного деплою:

1. Отримайте URL вашого додатку: `https://your-app-name.onrender.com`
2. Встановіть webhook для бота:
```bash
curl -X POST https://your-app-name.onrender.com/set_webhook \
  -H "Content-Type: application/json" \
  -d '{"url": "https://your-app-name.onrender.com/webhook"}'
```

Або використайте Postman/Browser:
- URL: `https://your-app-name.onrender.com/set_webhook`
- Method: POST
- Body (JSON): `{"url": "https://your-app-name.onrender.com/webhook"}`

## Крок 6: Перевірка

```bash
# Health check
curl https://your-app-name.onrender.com/api/health

# Очікуваний відповідь:
# {"status": "ok", "message": "Render server is running"}
```

## Крок 7: Keep-Alive (для Free Tier)

Free plan на Render засинає після 15 хвилин неактивності. Щоб уникнути:

### Варіант 1: UptimeRobot (рекомендовано)
1. Створіть безкоштовний аккаунт на [UptimeRobot](https://uptimerobot.com)
2. Додайте моніторинг для вашого URL
3. Налаштуйте перевірку кожні 5 хвилин
4. Keep-Alive автоматичний!

### Варіант 2: Cron Job
```bash
# Використайте будь-який безкоштовний cron service:
# - cron-job.org
# - easycron.com
# - cronitor.io

# URL для ping:
https://your-app-name.onrender.com/keep-alive
```

## Troubleshooting

### Помилка: "ModuleNotFoundError"
Перевірте, що всі залежності є в `requirements.txt`

### Помилка: "No database connection"
- Перевірте, що Database URL правильний
- Використовуйте **Internal Database URL**, не External

### Помилка: "Port already in use"
- Render автоматично встановлює PORT - не змінюйте його
- Використовуйте `os.getenv("PORT")` в коді

### App засинає
- Налаштуйте Keep-Alive (див. Крок 7)
- Або оновіть до Paid plan

### База даних не ініціалізується
```bash
# Перевірте логи на Render Dashboard
# Можливо потрібно додати SSL mode:
DATABASE_URL=postgresql://...?sslmode=require
```

## Полезні посилання:
- [Render Docs](https://render.com/docs)
- [PostgreSQL Guide](https://render.com/docs/databases)
- [Free Tier Limits](https://render.com/docs/free)

## Support
Якщо щось не працює - пишіть в Telegram: @your_support
