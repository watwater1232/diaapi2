# ⚡ Quick Start - Деплой на Render

## Швидкий чеклист (5 хвилин)

### ✅ 1. Підготовка файлів
- [x] `Procfile` - створено
- [x] `render.yaml` - створено  
- [x] `.gitignore` - налаштовано
- [x] `requirements.txt` - оновлено

### ✅ 2. Push на GitHub
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### ✅ 3. Створити Database на Render
1. [Render Dashboard](https://dashboard.render.com) → New + → PostgreSQL
2. Name: `diia-db`, Plan: Free
3. Скопіювати **Internal Database URL**

### ✅ 4. Створити Web Service
1. New + → Web Service → Connect GitHub repo
2. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py flask`
3. Environment Variables:
   ```
   DATABASE_URL=<Internal URL from step 3>
   CLOUDINARY_URL=cloudinary://...
   BOT_TOKEN=...
   ADMIN_IDS=...
   PYTHON_VERSION=3.11.0
   ```
4. Plan: Free → Create

### ✅ 5. Очікати деплой (~5-10 хв)
Перевірити логи на Render Dashboard

### ✅ 6. Налаштувати Webhook
```bash
curl -X POST https://your-app.onrender.com/set_webhook \
  -H "Content-Type: application/json" \
  -d '{"url": "https://your-app.onrender.com/webhook"}'
```

### ✅ 7. Перевірити
```bash
curl https://your-app.onrender.com/api/health
# Expected: {"status": "ok", "message": "Render server is running"}
```

### ✅ 8. Keep-Alive (опціонально)
- Або налаштуйте [UptimeRobot](https://uptimerobot.com)
- Або використайте `/keep-alive` endpoint

---

## 📱 Що потрібно мати:

### Telegram Bot Token
- Напишіть [@BotFather](https://t.me/BotFather)
- Команда: `/newbot`
- Скопіюйте токен

### Cloudinary Account
1. [cloudinary.com](https://cloudinary.com) - реєстрація
2. Dashboard → Account Details
3. Скопіюйте `CLOUDINARY_URL`

### Your Telegram ID
- Напишіть [@userinfobot](https://t.me/userinfobot)
- Скопіюйте ID

---

## 🔗 Посилання
- [Render Dashboard](https://dashboard.render.com)
- [Детальна інструкція](RENDER_DEPLOY.md)
- [UptimeRobot](https://uptimerobot.com)

---

## ❓ Проблеми?

**Error: Database connection failed**
→ Використайте Internal Database URL, не External

**Error: Module not found**
→ Перевірте `requirements.txt`

**App засинає**
→ Налаштуйте Keep-Alive через UptimeRobot

**Більше деталей:** Дивіться [RENDER_DEPLOY.md](RENDER_DEPLOY.md)
