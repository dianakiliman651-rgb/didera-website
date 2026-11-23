"""Усі тексти бота чотирма мовами. Ціни міняти тут: PRICE_SITE і PRICE_BOT."""

LANGS = ("uk", "ru", "cs", "en")
LANG_NAMES = {"uk": "🇺🇦 Українська", "ru": "Русский", "cs": "🇨🇿 Čeština", "en": "🇬🇧 English"}

PRICE_SITE = "250–350 €"
PRICE_BOT = "450–1100 €"

# Проєкти з портфоліо. Ключ = slug для посилань t.me/<бот>?start=p_<slug>
PROJECTS = {
    "marinek": "MARINEK",
    "mistrfix": "MISTR FIX",
    "maison": "MAISON ROUGE",
    "alloro": "ALLORO",
    "donut": "The Donut Experience",
    "raspberry": "Raspberry Atelier",
    "aurea": "AUREA",
    "woodspace": "Woodspace",
    "pylypiak": "PYLYPIAK",
    "iryna": "IRYNA BODLAK",
}

T = {
    "uk": {
        "hello_site": "Привіт! Дякую, що зазирнули в портфоліо 🤍 Кілька коротких питань, і заявка готова.",
        "hello": "Привіт! Я помічниця DIDÉRA 🤍\nДопоможу залишити заявку на сайт або Telegram-бота. Це займе хвилину.\n\nЩо вам ближче?",
        "hello_project": "Привіт! Бачу, вам сподобався проєкт <b>{project}</b> 🤍\nЗробимо щось подібне для вас. Кілька коротких питань.",
        "m_like": "🖼 Хочу сайт, як у портфоліо",
        "m_own": "✍️ Опишу свій сайт",
        "m_question": "💬 Просто запитати",
        "pick_project": "Який проєкт вам сподобався?",
        "describe": "Розкажіть про ваш сайт: чим ви займаєтесь, що має бути на сайті, які є приклади чи побажання. Можна одним повідомленням або голосовим.",
        "package": "Що вам потрібно?\n\n<b>Сайт</b>: {site}\n<b>Сайт + Telegram-бот</b> (заявки, оплата, автоматизація): {bot}\n\nЦіни орієнтовні, точну суму скажу після розмови.",
        "p_site": "🌐 Сайт · {site}",
        "p_bot": "🤖 Сайт + бот · {bot}",
        "p_unsure": "🤔 Ще не знаю, порадьте",
        "wishes": "Що б ви хотіли змінити чи додати? Напишіть кілька слів або натисніть «Пропустити».",
        "skip": "Пропустити →",
        "contact": "Як із вами зв'язатися? Натисніть кнопку, щоб поділитися номером, або напишіть телефон чи email. Якщо зручно в Telegram, просто натисніть «Пропустити».",
        "share_phone": "📱 Поділитися номером",
        "summary": "Перевірте, будь ласка:\n\n{body}\n\nНадсилаю?",
        "send": "✅ Надіслати",
        "restart": "↺ Почати знову",
        "done": "Дякую! Заявку отримала 🤍 Напишу вам найближчим часом.\n\nА поки можна ще раз подивитися портфоліо.",
        "ask_question": "Напишіть ваше запитання, я передам його Діані.",
        "question_sent": "Дякую! Діана відповість вам тут, у Telegram.",
        "prices": "Орієнтовні ціни:\n\n🌐 Сайт: <b>{site}</b>\n🤖 Сайт + Telegram-бот: <b>{bot}</b>\n\nТочна сума залежить від задачі. Натисніть /start, щоб залишити заявку.",
        "f_type": "Запит", "f_like": "Як у портфоліо: {p}", "f_own": "Свій сайт", "f_question": "Питання",
        "f_package": "Пакет", "f_desc": "Опис", "f_contact": "Контакт", "f_tg": "у Telegram",
        "pk_site": "Сайт ({site})", "pk_bot": "Сайт + бот ({bot})", "pk_unsure": "Ще не знаю",
        "portfolio": "Портфоліо DIDÉRA",
        "lang": "🌐 Мова",
        "choose_lang": "Оберіть мову:",
        "use_buttons": "Скористайтеся кнопками нижче 👇",
    },
    "ru": {
        "hello_site": "Привет! Спасибо, что заглянули в портфолио 🤍 Пара коротких вопросов, и заявка готова.",
        "hello": "Привет! Я помощница DIDÉRA 🤍\nПомогу оставить заявку на сайт или Telegram-бота. Это займёт минуту.\n\nЧто вам ближе?",
        "hello_project": "Привет! Вижу, вам понравился проект <b>{project}</b> 🤍\nСделаем что-то похожее для вас. Несколько коротких вопросов.",
        "m_like": "🖼 Хочу сайт, как в портфолио",
        "m_own": "✍️ Опишу свой сайт",
        "m_question": "💬 Просто спросить",
        "pick_project": "Какой проект вам понравился?",
        "describe": "Расскажите о вашем сайте: чем вы занимаетесь, что должно быть на сайте, есть ли примеры или пожелания. Можно одним сообщением или голосовым.",
        "package": "Что вам нужно?\n\n<b>Сайт</b>: {site}\n<b>Сайт + Telegram-бот</b> (заявки, оплата, автоматизация): {bot}\n\nЦены ориентировочные, точную сумму скажу после разговора.",
        "p_site": "🌐 Сайт · {site}",
        "p_bot": "🤖 Сайт + бот · {bot}",
        "p_unsure": "🤔 Пока не знаю, подскажите",
        "wishes": "Что бы вы хотели изменить или добавить? Напишите пару слов или нажмите «Пропустить».",
        "skip": "Пропустить →",
        "contact": "Как с вами связаться? Нажмите кнопку, чтобы поделиться номером, или напишите телефон либо email. Если удобно в Telegram, просто нажмите «Пропустить».",
        "share_phone": "📱 Поделиться номером",
        "summary": "Проверьте, пожалуйста:\n\n{body}\n\nОтправляю?",
        "send": "✅ Отправить",
        "restart": "↺ Начать заново",
        "done": "Спасибо! Заявку получила 🤍 Напишу вам в ближайшее время.\n\nА пока можно ещё раз посмотреть портфолио.",
        "ask_question": "Напишите ваш вопрос, я передам его Диане.",
        "question_sent": "Спасибо! Диана ответит вам здесь, в Telegram.",
        "prices": "Ориентировочные цены:\n\n🌐 Сайт: <b>{site}</b>\n🤖 Сайт + Telegram-бот: <b>{bot}</b>\n\nТочная сумма зависит от задачи. Нажмите /start, чтобы оставить заявку.",
        "f_type": "Запрос", "f_like": "Как в портфолио: {p}", "f_own": "Свой сайт", "f_question": "Вопрос",
        "f_package": "Пакет", "f_desc": "Описание", "f_contact": "Контакт", "f_tg": "в Telegram",
        "pk_site": "Сайт ({site})", "pk_bot": "Сайт + бот ({bot})", "pk_unsure": "Пока не знаю",
        "portfolio": "Портфолио DIDÉRA",
        "lang": "🌐 Язык",
        "choose_lang": "Выберите язык:",
        "use_buttons": "Воспользуйтесь кнопками ниже 👇",
    },
    "cs": {
        "hello_site": "Ahoj! Díky, že jste se podívali do portfolia 🤍 Pár krátkých otázek a poptávka je hotová.",
        "hello": "Ahoj! Jsem asistentka DIDÉRA 🤍\nPomůžu vám poslat poptávku na web nebo Telegram bota. Zabere to minutu.\n\nCo je vám bližší?",
        "hello_project": "Ahoj! Vidím, že se vám líbí projekt <b>{project}</b> 🤍\nUděláme pro vás něco podobného. Pár krátkých otázek.",
        "m_like": "🖼 Chci web jako v portfoliu",
        "m_own": "✍️ Popíšu svůj web",
        "m_question": "💬 Jen se zeptat",
        "pick_project": "Který projekt se vám líbí?",
        "describe": "Řekněte mi o svém webu: čím se zabýváte, co má na webu být, máte příklady nebo přání? Klidně jednou zprávou nebo hlasovkou.",
        "package": "Co potřebujete?\n\n<b>Web</b>: {site}\n<b>Web + Telegram bot</b> (poptávky, platby, automatizace): {bot}\n\nCeny jsou orientační, přesnou částku řeknu po domluvě.",
        "p_site": "🌐 Web · {site}",
        "p_bot": "🤖 Web + bot · {bot}",
        "p_unsure": "🤔 Ještě nevím, poraďte",
        "wishes": "Co byste chtěli změnit nebo přidat? Napište pár slov nebo klikněte na „Přeskočit“.",
        "skip": "Přeskočit →",
        "contact": "Jak vás mohu kontaktovat? Klikněte na tlačítko a sdílejte číslo, nebo napište telefon či e-mail. Pokud vám vyhovuje Telegram, stačí „Přeskočit“.",
        "share_phone": "📱 Sdílet číslo",
        "summary": "Zkontrolujte prosím:\n\n{body}\n\nOdeslat?",
        "send": "✅ Odeslat",
        "restart": "↺ Začít znovu",
        "done": "Děkuji! Poptávku mám 🤍 Brzy se vám ozvu.\n\nMezitím se můžete znovu podívat do portfolia.",
        "ask_question": "Napište svou otázku, předám ji Dianě.",
        "question_sent": "Děkuji! Diana vám odpoví tady v Telegramu.",
        "prices": "Orientační ceny:\n\n🌐 Web: <b>{site}</b>\n🤖 Web + Telegram bot: <b>{bot}</b>\n\nPřesná částka záleží na zadání. Klikněte na /start a pošlete poptávku.",
        "f_type": "Poptávka", "f_like": "Jako v portfoliu: {p}", "f_own": "Vlastní web", "f_question": "Otázka",
        "f_package": "Balíček", "f_desc": "Popis", "f_contact": "Kontakt", "f_tg": "v Telegramu",
        "pk_site": "Web ({site})", "pk_bot": "Web + bot ({bot})", "pk_unsure": "Ještě nevím",
        "portfolio": "Portfolio DIDÉRA",
        "lang": "🌐 Jazyk",
        "choose_lang": "Vyberte jazyk:",
        "use_buttons": "Použijte prosím tlačítka níže 👇",
    },
    "en": {
        "hello_site": "Hi! Thanks for looking through the portfolio 🤍 A few quick questions and your request is ready.",
        "hello": "Hi! I'm the DIDÉRA assistant 🤍\nI'll help you send a request for a website or a Telegram bot. It takes a minute.\n\nWhat fits you best?",
        "hello_project": "Hi! I see you liked <b>{project}</b> 🤍\nLet's make something like it for you. A few quick questions.",
        "m_like": "🖼 A site like one in the portfolio",
        "m_own": "✍️ I'll describe my own site",
        "m_question": "💬 Just a question",
        "pick_project": "Which project did you like?",
        "describe": "Tell me about your site: what you do, what should be on it, any examples or wishes. One message or a voice note is fine.",
        "package": "What do you need?\n\n<b>Website</b>: {site}\n<b>Website + Telegram bot</b> (requests, payments, automation): {bot}\n\nPrices are approximate; I'll give the exact figure after we talk.",
        "p_site": "🌐 Website · {site}",
        "p_bot": "🤖 Site + bot · {bot}",
        "p_unsure": "🤔 Not sure yet, advise me",
        "wishes": "Anything you'd like to change or add? Write a few words or tap “Skip”.",
        "skip": "Skip →",
        "contact": "How can I reach you? Tap the button to share your number, or type a phone or email. If Telegram is fine, just tap “Skip”.",
        "share_phone": "📱 Share my number",
        "summary": "Please check:\n\n{body}\n\nSend it?",
        "send": "✅ Send",
        "restart": "↺ Start over",
        "done": "Thank you! I've got your request 🤍 I'll get back to you soon.\n\nMeanwhile, feel free to look through the portfolio again.",
        "ask_question": "Type your question and I'll pass it to Diana.",
        "question_sent": "Thank you! Diana will reply right here in Telegram.",
        "prices": "Approximate prices:\n\n🌐 Website: <b>{site}</b>\n🤖 Website + Telegram bot: <b>{bot}</b>\n\nThe exact figure depends on the task. Tap /start to send a request.",
        "f_type": "Request", "f_like": "Like in portfolio: {p}", "f_own": "Own site", "f_question": "Question",
        "f_package": "Package", "f_desc": "Description", "f_contact": "Contact", "f_tg": "via Telegram",
        "pk_site": "Website ({site})", "pk_bot": "Website + bot ({bot})", "pk_unsure": "Not sure yet",
        "portfolio": "DIDÉRA portfolio",
        "lang": "🌐 Language",
        "choose_lang": "Choose a language:",
        "use_buttons": "Please use the buttons below 👇",
    },
}


def t(lang: str, key: str, **kw) -> str:
    s = T.get(lang, T["uk"])[key]
    return s.format(site=PRICE_SITE, bot=PRICE_BOT, **kw)


def pick_lang(code: str | None) -> str:
    code = (code or "").lower()
    if code.startswith("ru"):
        return "ru"
    if code.startswith(("cs", "sk")):
        return "cs"
    if code.startswith("en"):
        return "en"
    return "uk"
