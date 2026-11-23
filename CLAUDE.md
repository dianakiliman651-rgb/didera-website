# Інструменти для створення сайтів

## Навички (`.claude/skills/`)
- **design-taste-frontend** (Taste Skill, github.com/Leonxlnx/taste-skill, MIT) — композиція, типографіка, відступи. Використовувати при створенні будь-якої сторінки чи секції.
- **emil-design-eng** (github.com/emilkowalski/skills) — анімації, стани кнопок, плавні переходи.

## Figma
Офіційний конектор Figma MCP (підключається в claude.ai → Connectors). Коли надіслано посилання на фрейм, читати макет інструментами `get_design_context`, `get_screenshot`, `get_variable_defs`.

## Перевірка в браузері
Chromium і Playwright уже є в хмарному образі. Скриншот з емуляцією телефона:

    node tools/shot.cjs <url|файл.html> [out.png] ["iPhone 15"] [--full]

Скрипт виводить розмір вікна, горизонтальне переповнення та помилки консолі.
Примітка: `playwright screenshot --device "iPhone ..."` не працює, бо профіль iPhone вимагає WebKit, якого в образі немає — використовуйте `tools/shot.cjs`.
