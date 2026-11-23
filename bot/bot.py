"""DIDÉRA: бот для заявок на сайти й Telegram-ботів.

Змінні середовища:
  BOT_TOKEN      токен від @BotFather (обов'язково)
  ADMIN_CHAT_ID  куди надсилати заявки: ваш chat id (дізнатися: напишіть боту /myid)
  PORTFOLIO_URL  посилання на портфоліо (необов'язково)
  DATA_DIR       куди писати leads.csv (за замовчуванням ./data)
"""
import asyncio
import csv
import html
import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from texts import LANG_NAMES, LANGS, PROJECTS, pick_lang, t

PORTFOLIO_URL = os.getenv("PORTFOLIO_URL", "https://claude.ai/artifact/L4fqe3JM3F3ettFTTbKb4Z")
DATA_DIR = Path(os.getenv("DATA_DIR", Path(__file__).parent / "data"))

router = Router()


class Lead(StatesGroup):
    menu = State()
    project = State()
    describe = State()
    package = State()
    wishes = State()
    contact = State()
    confirm = State()
    question = State()


def ikb(rows):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=a, callback_data=b) for a, b in r] for r in rows])


async def lang_of(state: FSMContext, user) -> str:
    d = await state.get_data()
    return d.get("lang") or pick_lang(getattr(user, "language_code", None))


def menu_kb(L):
    return ikb([
        [(t(L, "m_like"), "m:like")],
        [(t(L, "m_own"), "m:own")],
        [(t(L, "m_question"), "m:q")],
        [(t(L, "lang"), "lang")],
    ])


def package_kb(L):
    return ikb([
        [(t(L, "p_site"), "pk:site")],
        [(t(L, "p_bot"), "pk:bot")],
        [(t(L, "p_unsure"), "pk:unsure")],
    ])


# ---------- start / menu ----------

@router.message(CommandStart())
async def start(m: Message, state: FSMContext, command: CommandObject):
    old = await state.get_data()
    await state.clear()
    L = old.get("lang") or pick_lang(m.from_user.language_code)
    # deep link: ?start=p_iryna or ?start=p_iryna_ru or ?start=ru
    arg = (command.args or "").strip().lower()
    parts = arg.split("_") if arg else []
    if parts and parts[-1] in LANGS:
        L = parts.pop()
    await state.update_data(lang=L, media=[])
    if len(parts) >= 2 and parts[0] == "p" and parts[1] in PROJECTS:
        slug = parts[1]
        await state.update_data(kind="like", project=slug)
        await m.answer(t(L, "hello_project", project=PROJECTS[slug]))
        await state.set_state(Lead.package)
        await m.answer(t(L, "package"), reply_markup=package_kb(L))
        return
    await state.set_state(Lead.menu)
    await m.answer(t(L, "hello"), reply_markup=menu_kb(L))


@router.callback_query(F.data == "lang")
async def lang_menu(c: CallbackQuery, state: FSMContext):
    L = await lang_of(state, c.from_user)
    await c.message.edit_text(t(L, "choose_lang"), reply_markup=ikb([[(LANG_NAMES[x], "setlang:" + x)] for x in LANGS]))
    await c.answer()


@router.callback_query(F.data.startswith("setlang:"))
async def set_lang(c: CallbackQuery, state: FSMContext):
    L = c.data.split(":", 1)[1]
    await state.update_data(lang=L)
    await state.set_state(Lead.menu)
    await c.message.edit_text(t(L, "hello"), reply_markup=menu_kb(L))
    await c.answer()


@router.callback_query(F.data.startswith("m:"))
async def menu_pick(c: CallbackQuery, state: FSMContext):
    L = await lang_of(state, c.from_user)
    choice = c.data[2:]
    await c.answer()
    if choice == "like":
        await state.update_data(kind="like")
        await state.set_state(Lead.project)
        rows = [[(name, "pr:" + slug)] for slug, name in PROJECTS.items()]
        await c.message.edit_text(t(L, "pick_project"), reply_markup=ikb(rows))
    elif choice == "own":
        await state.update_data(kind="own")
        await state.set_state(Lead.describe)
        await c.message.edit_text(t(L, "describe"))
    else:
        await state.update_data(kind="question")
        await state.set_state(Lead.question)
        await c.message.edit_text(t(L, "ask_question"))


@router.callback_query(Lead.project, F.data.startswith("pr:"))
async def project_pick(c: CallbackQuery, state: FSMContext):
    L = await lang_of(state, c.from_user)
    slug = c.data[3:]
    await state.update_data(project=slug)
    await state.set_state(Lead.package)
    await c.message.edit_text(f"✔ <b>{PROJECTS.get(slug, slug)}</b>")
    await c.message.answer(t(L, "package"), reply_markup=package_kb(L))
    await c.answer()


# ---------- description (text, voice, photos, files) ----------

def remember_media(data, m: Message):
    media = list(data.get("media", []))
    if not m.text:
        media.append([m.chat.id, m.message_id])
    return media


def message_text(m: Message) -> str:
    return (m.text or m.caption or "").strip()


@router.message(Lead.describe)
async def got_description(m: Message, state: FSMContext):
    L = await lang_of(state, m.from_user)
    d = await state.get_data()
    desc = "\n".join(x for x in [d.get("desc", ""), message_text(m) or ("🎤/📎" if not m.text else "")] if x)
    await state.update_data(desc=desc, media=remember_media(d, m))
    await state.set_state(Lead.package)
    await m.answer(t(L, "package"), reply_markup=package_kb(L))


@router.callback_query(Lead.package, F.data.startswith("pk:"))
async def package_pick(c: CallbackQuery, state: FSMContext):
    L = await lang_of(state, c.from_user)
    pk = c.data[3:]
    await state.update_data(package=pk)
    await c.message.edit_text("✔ " + t(L, "pk_" + pk))
    await c.answer()
    d = await state.get_data()
    if d.get("kind") == "like":
        await state.set_state(Lead.wishes)
        await c.message.answer(t(L, "wishes"), reply_markup=ikb([[(t(L, "skip"), "skip")]]))
    else:
        await ask_contact(c.message, state, L)


@router.message(Lead.wishes)
async def got_wishes(m: Message, state: FSMContext):
    L = await lang_of(state, m.from_user)
    d = await state.get_data()
    await state.update_data(desc=message_text(m) or "🎤/📎", media=remember_media(d, m))
    await ask_contact(m, state, L)


@router.callback_query(Lead.wishes, F.data == "skip")
async def skip_wishes(c: CallbackQuery, state: FSMContext):
    L = await lang_of(state, c.from_user)
    await c.message.edit_reply_markup(reply_markup=None)
    await c.answer()
    await ask_contact(c.message, state, L)


# ---------- contact ----------

async def ask_contact(m: Message, state: FSMContext, L: str):
    await state.set_state(Lead.contact)
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=t(L, "share_phone"), request_contact=True)], [KeyboardButton(text=t(L, "skip"))]],
        resize_keyboard=True, one_time_keyboard=True,
    )
    await m.answer(t(L, "contact"), reply_markup=kb)


@router.message(Lead.contact)
async def got_contact(m: Message, state: FSMContext):
    L = await lang_of(state, m.from_user)
    if m.contact:
        contact = m.contact.phone_number
    elif m.text and m.text.strip() not in {t(x, "skip") for x in LANGS}:
        contact = m.text.strip()
    else:
        contact = ""
    await state.update_data(contact=contact)
    await state.set_state(Lead.confirm)
    d = await state.get_data()
    await m.answer("👌", reply_markup=ReplyKeyboardRemove())
    await m.answer(t(L, "summary", body=lead_body(d, L, m.from_user)),
                   reply_markup=ikb([[(t(L, "send"), "send")], [(t(L, "restart"), "restart")]]))


def lead_body(d: dict, L: str, user) -> str:
    e = html.escape
    kind = d.get("kind")
    if kind == "like":
        what = t(L, "f_like", p=PROJECTS.get(d.get("project"), d.get("project", "")))
    elif kind == "own":
        what = t(L, "f_own")
    else:
        what = t(L, "f_question")
    lines = [f"<b>{t(L, 'f_type')}:</b> {e(what)}"]
    if d.get("package"):
        lines.append(f"<b>{t(L, 'f_package')}:</b> {e(t(L, 'pk_' + d['package']))}")
    if d.get("desc"):
        lines.append(f"<b>{t(L, 'f_desc')}:</b> {e(d['desc'])}")
    contact = d.get("contact") or (("@" + user.username) if user.username else t(L, "f_tg"))
    lines.append(f"<b>{t(L, 'f_contact')}:</b> {e(contact)}")
    return "\n".join(lines)


@router.callback_query(Lead.confirm, F.data == "restart")
async def restart(c: CallbackQuery, state: FSMContext):
    L = await lang_of(state, c.from_user)
    await state.clear()
    await state.update_data(lang=L, media=[])
    await state.set_state(Lead.menu)
    await c.message.edit_text(t(L, "hello"), reply_markup=menu_kb(L))
    await c.answer()


@router.callback_query(Lead.confirm, F.data == "send")
async def send_lead(c: CallbackQuery, state: FSMContext, bot: Bot):
    L = await lang_of(state, c.from_user)
    d = await state.get_data()
    await c.message.edit_reply_markup(reply_markup=None)
    await c.answer("✅")
    await deliver(bot, c.from_user, d, L)
    await state.clear()
    await state.update_data(lang=L)
    await c.message.answer(t(L, "done"), reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=t(L, "portfolio"), url=PORTFOLIO_URL)]]))


# ---------- question ----------

@router.message(Lead.question)
async def got_question(m: Message, state: FSMContext, bot: Bot):
    L = await lang_of(state, m.from_user)
    d = await state.get_data()
    d.update(desc=message_text(m) or "🎤/📎", media=remember_media(d, m))
    await deliver(bot, m.from_user, d, L)
    await state.clear()
    await state.update_data(lang=L)
    await m.answer(t(L, "question_sent"))


# ---------- delivery to Diana ----------

async def deliver(bot: Bot, user, d: dict, L: str):
    name = html.escape(user.full_name or "—")
    who = f'<a href="tg://user?id={user.id}">{name}</a>' + (f" · @{user.username}" if user.username else "")
    head = "🔔 <b>Нова заявка</b>" if d.get("kind") != "question" else "💬 <b>Нове питання</b>"
    text = f"{head}\n{who} · {L.upper()}\n\n{lead_body(d, 'uk', user)}"
    save_csv(user, d, L)
    admin = os.getenv("ADMIN_CHAT_ID")
    if not admin:
        logging.warning("ADMIN_CHAT_ID не задано, заявка лише в CSV:\n%s", text)
        return
    kb = None
    if user.username:
        kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Написати ↗", url=f"https://t.me/{user.username}")]])
    await bot.send_message(int(admin), text, reply_markup=kb)
    for chat_id, msg_id in d.get("media", []):
        try:
            await bot.copy_message(int(admin), chat_id, msg_id)
        except Exception:  # noqa: BLE001
            logging.exception("не вдалося переслати вкладення")


def save_csv(user, d: dict, L: str):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    f = DATA_DIR / "leads.csv"
    new = not f.exists()
    with f.open("a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["time_utc", "user_id", "username", "name", "lang", "kind", "project", "package", "description", "contact"])
        w.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"), user.id, user.username or "", user.full_name,
                    L, d.get("kind", ""), d.get("project", ""), d.get("package", ""), d.get("desc", ""), d.get("contact", "")])


# ---------- utility commands ----------

@router.message(Command("prices"))
async def prices(m: Message, state: FSMContext):
    await m.answer(t(await lang_of(state, m.from_user), "prices"))


@router.message(Command("myid"))
async def myid(m: Message):
    await m.answer(f"Ваш chat id: <code>{m.chat.id}</code>")


@router.message()
async def fallback(m: Message, state: FSMContext):
    L = await lang_of(state, m.from_user)
    if await state.get_state() is None:
        await state.update_data(lang=L, media=[])
        await state.set_state(Lead.menu)
        await m.answer(t(L, "hello"), reply_markup=menu_kb(L))
    else:
        await m.answer(t(L, "use_buttons"))


def build_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(router)
    return dp


async def main():
    logging.basicConfig(level=logging.INFO)
    token = os.environ["BOT_TOKEN"]
    bot = Bot(token, default=DefaultBotProperties(parse_mode="HTML"))
    from aiogram.types import BotCommand
    for L in LANGS:
        await bot.set_my_commands(
            [BotCommand(command="start", description={"uk": "Залишити заявку", "ru": "Оставить заявку", "cs": "Poslat poptávku", "en": "Send a request"}[L]),
             BotCommand(command="prices", description={"uk": "Ціни", "ru": "Цены", "cs": "Ceny", "en": "Prices"}[L])],
            language_code=None if L == "uk" else L)
    await build_dispatcher().start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
