import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
import asyncio
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser


sython.start()

LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await sython(JoinChannelRequest("@SAYTHONH"))
    except BaseException:
        pass
 
 
GCAST_BLACKLIST = [
    -1001884452589,
    -1001884452589,
]

DEVS = [
    5159123009,
]

def calc(num1, num2, fun):
    if fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "X":
        return num1 * num2
    elif fun == "x":
        return num1 * num2
    elif fun == "/":
        return num1 / num2
    elif fun == "÷":
        return num1 / num2
    else:
        return "خطأ"


@sython.on(events.NewMessage(outgoing=True, pattern=".احسب (.*)"))
async def _(event):
    try:
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        num1 = int(msg[0])
        num2 = int(msg[2])
        fun = str(msg[1])
        await event.edit(f''' الناتج = `{calc(num1, num2, fun)}`''')
    except:
        await event.edit('''خطأ, يرجى ادخال الرقم مثل :
7 + 7
7 - 7
7 x 7
7 ÷ 7''')


from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from config import *
import asyncio
from telethon import events

c = requests.session()
bot_username = '@t06bot'


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@t06bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@t06bot', '/start')
        await asyncio.sleep(10)
        msg0 = await sython.get_messages('@t06bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(10)
        msg1 = await sython.get_messages('@t06bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(10)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@t06bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sython.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython.on(events.NewMessage(outgoing=True, pattern=".للكروبات(?: |$)(.*)"))
async def gcast(event):
    sython = event.pattern_match.group(1)
    if sython:
        msg = sython
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )


@sython.on(events.NewMessage(outgoing=True, pattern=".للخاص(?: |$)(.*)"))
async def gucast(event):
    sython = event.pattern_match.group(1)
    if sython:
        msg = sython
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )

@sython.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@sython.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
 
    
@sython.on(events.NewMessage(outgoing=True, pattern=".فحص"))
async def _(event):
      await event.reply("""السـورس يعمـل | 𝐒𝐘𝐓𝐇𝐎𝐍
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

- المطور : حسام فوزي | SOMY

- سورس بسيط يحتوي على الاوامر المهمة التي تحتاجها

قناة السورس : https://t.me/SAYTHONH
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍"""
)

@sython.on(events.NewMessage(outgoing=True, pattern=".مطور"))
async def _(event):
      await event.reply("""SY OWNER : @T_4_Z"""
)

@sython.on(events.NewMessage(outgoing=True, pattern=".حلويات"))
async def _(event):
    event = await event.edit("candy")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)

@sython.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

@sython.on(events.NewMessage(outgoing=True, pattern=".العد التنازلي"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🔟")
    animation_chars = [
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",

    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

        
@sython.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@sython.on(events.NewMessage(outgoing=True, pattern=".قمور"))
async def _(event):
    event = await event.edit("قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])

@sython.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""اوامر السورس | 𝐒𝐘𝐓𝐇𝐎𝐍

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

1️⃣ الامـر فحص
الوظيفة : فحص السورس 
طريقة الاستخدام [`.فحص`]

2️⃣ الامـر نشر تلقائي
الوظيفة : نشر رسالة معينة تلقائيا
طريقة الاستعمال : 
[.مؤقت + عدد الثواني + عدد التكرار + الكليشة]

مثال | [`.مؤقت 3 5 مرحبأ بك في سورس سايثون` ]

3️⃣ الامر [تكرار] 
الوظيفة : تكرار رسالة معينة بالرد عليها 
طريقة الاستعمال : .تكرار + عدد التكرار 

4️⃣ الامر اذاعة للخاص 
الوظيفة : ارسال رسالة معينة الى جميع المحادثات الخاصة في حسابك
طريقة الاستعمال : .للخاص + الكليشة
مثال | `.للخاص مرحبا بك في سورس سايثون `

5️⃣ الامر اذاعة للمجموعات
الوظيفة : ارسال رسالة معينة الى جميع المجموعات في حسابك
طريقة الاستعمال : .للكروبات + الكليشة
مثال | `.للخاص مرحبا بك في سورس سايثون `

6️⃣ الامر تسلية 
الوظيفة : التسلية فقط 
محتويات الامر : 
[`.قمور`]
[`.حلويات`]
[`.قلوب`]
[`.العد التنازلي`]
[`.قمر`]

7️⃣ الامر الالة الحاسبة العلمية 
طريقة الاستعمال 
[`.احسب + الرقم الاول + العملية الحسابية + الرقم الثاني` ]
يجب مراعات المسافة بين كل كلمة
`مثال | .احسب 7 + 7 `
`مثال | .احسب 7 * 7 ` 
`مثال | .احسب 7 - 7  `
`مثال | .احسب 7 ÷ 7 `

8️⃣ الامر تجميع نقاط بوت المليار 
الوظيفة : يستخدم لتجميع نقاط بوت تمويل المليار تلقائيا 

طريقة التشغيل : `.تجميع المليار`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝙱𝚈 𝙷𝚄𝚂𝚂𝙰𝙼.𝙵𝙰""")
     



print("🔶 SYTHON WORKING 🔶 ")


sython.run_until_disconnected()
sython.loop.create_task(join_channel())


