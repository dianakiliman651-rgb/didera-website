# DIDÉRA: бот для заявок

Клієнт пише боту, а бот питає:
1. **Що потрібно**: «Хочу сайт, як у портфоліо» (вибір із 10 проєктів), «Опишу свій сайт» (текст, голосове, фото) або «Просто запитати».
2. **Пакет**: Сайт **250–350 €** · Сайт + Telegram-бот **450–1100 €** · «Ще не знаю».
3. **Побажання** (для проєкту з портфоліо, можна пропустити).
4. **Контакт**: кнопка «Поділитися номером», телефон/email текстом або просто Telegram.
5. Перевірка заявки, кнопка «Надіслати».

Заявка приходить вам у Telegram (з кнопкою «Написати») і зберігається в `data/leads.csv`.
Голосові та фото, які надіслав клієнт, бот пересилає вам слідом за заявкою.

Мови: українська, російська, чеська, англійська. Бот бере мову з Telegram людини, а в меню її можна змінити.
Команди: `/start` (заявка), `/prices` (ціни), `/myid` (показує ваш chat id).

## Посилання з портфоліо

- `https://t.me/<бот>?start=p_iryna`: людина одразу потрапляє на «Як у портфоліо: IRYNA BODLAK».
- Мову можна додати в кінці: `?start=p_iryna_ru`, `p_marinek_cs`, `p_aurea_en`.
- Назви проєктів: marinek, mistrfix, maison, alloro, donut, raspberry, aurea, woodspace, pylypiak, iryna.

## Запуск

1. У [@BotFather](https://t.me/BotFather): `/newbot`, задайте назву й username, скопіюйте **токен**.
2. Запустіть бота з `BOT_TOKEN`, напишіть йому `/myid` і скопіюйте число.
3. Перезапустіть із `ADMIN_CHAT_ID=<це число>`. Тепер заявки приходять вам.

```bash
pip install -r requirements.txt
BOT_TOKEN=123:ABC ADMIN_CHAT_ID=111111 python bot.py
```

Боту потрібен сервер, який працює цілодобово. Підійде будь-який хостинг із Docker
(Railway, Render Background Worker, Fly.io, VPS):

```bash
docker build -t didera-bot .
docker run -d --restart=always -e BOT_TOKEN=... -e ADMIN_CHAT_ID=... -v $PWD/data:/app/data didera-bot
```

Ціни й тексти змінюються в `texts.py` (`PRICE_SITE`, `PRICE_BOT`).

## Перевірка без Telegram

```bash
python tests/test_flow.py
```
