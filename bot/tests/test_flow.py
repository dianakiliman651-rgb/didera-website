"""Прогін сценаріїв без мережі: фейкова сесія записує, що бот надсилає."""
import asyncio, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ["ADMIN_CHAT_ID"] = "999"
os.environ["DATA_DIR"] = tempfile.mkdtemp()
from datetime import datetime
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.base import BaseSession
from aiogram.methods import TelegramMethod
from aiogram.types import Update, Message, Chat, User, CallbackQuery, Contact
import bot as B

class Fake(BaseSession):
    def __init__(self): super().__init__(); self.sent=[]
    async def make_request(self, bot, method, timeout=None):
        self.sent.append(method)
        rt = method.__returning__
        name = type(method).__name__
        if name in ("SendMessage","EditMessageText","EditMessageReplyMarkup","CopyMessage") and rt is not bool:
            if name=="CopyMessage":
                from aiogram.types import MessageId; return MessageId(message_id=1)
            return Message(message_id=len(self.sent), date=datetime.now(), chat=Chat(id=getattr(method,'chat_id',1) or 1,type="private"), text="x")
        return True
    async def close(self): pass
    async def stream_content(self,*a,**k): yield b""

U = User(id=42, is_bot=False, first_name="Olena", username="olena", language_code="ru")
CH = Chat(id=42, type="private")
n = [0]
def upd(**kw): n[0]+=1; return Update(update_id=n[0], **kw)
def msg(text=None, **kw): n[0]+=1; return upd(message=Message(message_id=n[0], date=datetime.now(), chat=CH, from_user=U, text=text, **kw))
def cb(data): return upd(callback_query=CallbackQuery(id=str(n[0]), from_user=U, chat_instance="c", data=data,
    message=Message(message_id=5, date=datetime.now(), chat=CH, text="x")))

def texts(s, start):
    out=[]
    for m in s.sent[start:]:
        t=getattr(m,'text',None)
        if t: out.append((type(m).__name__, getattr(m,'chat_id',None), t.replace("\n"," | ")[:150]))
    return out

async def run(name, steps):
    s=Fake(); bot=Bot("1:x", session=s, default=DefaultBotProperties(parse_mode="HTML")); B.router._parent_router=None; dp=B.build_dispatcher()
    print("=== "+name)
    for st in steps:
        k=len(s.sent); await dp.feed_update(bot, st)
        for x in texts(s,k): print("  ",x)
    return s

async def main():
    s=await run("own site, RU, phone", [msg("/start"), cb("m:own"), msg("Салон красоты в Праге, нужна запись онлайн"), cb("pk:bot"),
        msg(contact=Contact(phone_number="+420111222333", first_name="Olena")), cb("send")])
    assert any(getattr(m,'chat_id',None)==999 and "Салон" in m.text for m in s.sent if hasattr(m,'text') and m.text)
    s=await run("deep link iryna", [msg("/start p_iryna_cs"), cb("pk:site"), cb("skip"), msg("Přeskočit →"), cb("send")])
    assert any(getattr(m,'chat_id',None)==999 and "IRYNA" in m.text for m in s.sent if getattr(m,'text',None))
    s=await run("portfolio pick + wishes + lang switch", [msg("hello"), cb("lang"), cb("setlang:uk"), cb("m:like"), cb("pr:marinek"), cb("pk:unsure"), msg("Хочу інші кольори"), msg("olena@mail.cz"), cb("send")])
    s=await run("question", [msg("/start"), cb("m:q"), msg("Скільки займає розробка?")])
    s=await run("random text mid-flow + prices", [msg("/start"), msg("???"), msg("/prices")])
    print(open(os.path.join(os.environ["DATA_DIR"],"leads.csv")).read())
asyncio.run(main())
