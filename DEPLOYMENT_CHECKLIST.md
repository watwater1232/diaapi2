# ✅ Deployment Checklist

## 📁 Файли для деплою (перевірити)

### Обов'язкові файли:
- [x] `Procfile` - команда запуску для Render
- [x] `requirements.txt` - Python залежності
- [x] `render.yaml` - конфігурація Render (опціонально)
- [x] `.gitignore` - щоб не комітити .env

### Документація:
- [x] `README.md` - головний файл
- [x] `QUICKSTART.md` - швидкий старт
- [x] `RENDER_DEPLOY.md` - детальна інструкція
- [x] `DEPLOYMENT_CHECKLIST.md` - цей файл

### Код:
- [x] `main.py` - точка входу з підтримкою Flask mode
- [x] `render_server.py` - Flask сервер для Render
- [x] `api/main.py` - FastAPI endpoints
- [x] `database/models.py` - моделі БД
- [x] `api/admin.py` - admin routes

### Конфігурація:
- [x] `env_example.txt` - приклад змінних оточення
- [x] `.env` - НЕ комітити! (в .gitignore)

---

## 🚀 Кроки деплою

### Pre-deployment:
- [ ] Перевірити, що всі файли збережені
- [ ] Перевірити `.gitignore` (`.env` має бути там)
- [ ] Створити `.env` локально для тестів
- [ ] Протестувати локально: `python main.py`

### GitHub:
- [ ] `git add .`
- [ ] `git commit -m "Ready for Render deployment"`
- [ ] `git push origin main`

### Render - Database:
- [ ] Створити PostgreSQL database
- [ ] Скопіювати Internal Database URL
- [ ] Зберегти URL для наступного кроку

### Render - Web Service:
- [ ] New + → Web Service
- [ ] Підключити GitHub репозиторій
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `python main.py flask`
- [ ] Runtime: Python 3
- [ ] Plan: Free

### Environment Variables:
- [ ] `DATABASE_URL` = Internal URL з database
- [ ] `CLOUDINARY_URL` = з Cloudinary dashboard
- [ ] `BOT_TOKEN` = з @BotFather
- [ ] `ADMIN_IDS` = ваш Telegram ID
- [ ] `CRYPTOPAY_TOKEN` = (опціонально)
- [ ] `PYTHON_VERSION` = 3.11.0

### Post-deployment:
- [ ] Чекати завершення build (~5-10 хв)
- [ ] Перевірити logs
- [ ] Health check: `curl https://your-app.onrender.com/api/health`
- [ ] Налаштувати webhook для бота
- [ ] Налаштувати Keep-Alive (UptimeRobot)

---

## 🔍 Тестування після деплою

### 1. Health Check:
```bash
curl https://your-app.onrender.com/api/health
# Expected: {"status": "ok", "message": "Render server is running"}
```

### 2. Keep-Alive:
```bash
curl https://your-app.onrender.com/keep-alive
# Expected: {"status": "ok", "message": "Server is alive"}
```

### 3. Webhook Setup:
```bash
curl -X POST https://your-app.onrender.com/set_webhook \
  -H "Content-Type: application/json" \
  -d '{"url": "https://your-app.onrender.com/webhook"}'
```

### 4. Test Bot:
- Напишіть боту в Telegram
- Перевірте, що він відповідає

---

## ❌ Часті помилки

### "ModuleNotFoundError"
**Причина:** Пакет не в `requirements.txt`  
**Рішення:** Додайте в `requirements.txt` з версією

### "Database connection failed"
**Причина:** Неправильний DATABASE_URL  
**Рішення:** Використайте Internal Database URL, не External

### "Port already in use"
**Причина:** Хардкод port в коді  
**Рішення:** Використайте `os.getenv("PORT")` завжди

### "App засинає через 15 хвилин"
**Причина:** Free tier на Render  
**Рішення:** Налаштуйте Keep-Alive через UptimeRobot

### "No such file or directory: database/"
**Причина:** SQLite намагається створити директорію  
**Рішення:** Використайте PostgreSQL на Render

---

## 📞 Support

Якщо щось не працює:
1. Перевірте логи на Render Dashboard
2. Перевірте всі Environment Variables
3. Перевірте `QUICKSTART.md` і `RENDER_DEPLOY.md`
4. Перевірте Health check endpoint
5. Перевірте database connection

---

## 📝 Нотатки

- Free tier має обмеження (CPU, RAM, sleep)
- Keep-Alive важливий для free tier
- PostgreSQL на Render безкоштовний
- Всі sensitive дані в Environment Variables
- `.env` ніколи не комітити в Git!

---

**Успіхів з деплоєм! 🚀**
