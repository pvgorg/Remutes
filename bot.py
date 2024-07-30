#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os, asyncio
import random as ra
from pyrogram import Client, filters, errors
from pyrogram.enums import ParseMode
from pyrogram.raw import functions, types

bot_token = "7199644794:AAGNC5KDIV2PREO-3cDWk8KHqS8Dawp8NCM"
sudo = 6558631633
login_temp_list = {}

if not os.path.isdir('Rimots') : os.mkdir('Rimots')
if not os.path.isdir('downloads') : os.mkdir('downloads')
if not os.path.exists('downloads/time.txt') :
    with open('downloads/time.txt', 'w', encoding="utf-8") as file :
        file.write('5')

async def sleep(time):
    await asyncio.sleep(time)


def app_info() :
    with open('app_info.txt', 'r') as file :
        return ra.choice(file.read().split('\n')).split()

def getAccount() :
    return [f.split('.')[0] for f in os.listdir('Rimots') if os.path.isfile(os.path.join('Rimots', f))]

bot = Client(
    "bot",
    bot_token = bot_token,
    api_id = "12176206",
    api_hash = "b8eff20a7e8adcdaa3daa3bc789a5b41"
)

@bot.on_message(filters.command(["start"]) & filters.user(sudo))
async def start(client, message):
    await bot.send_message(message.from_user.id,'''<b>Welcome to MurDer Army </b>
<b>Atakeri</b>

<u>🟢 راهنمای افزودن اکانت به ربات 🟢</u>

<b>🟡 با استفاده از دستور زیر کد ، یک کد پنج رقمی برای اکانت مورد نظر ارسال میشه :</b>
⚪️ <code>/add</code> +989999999999 ⚪️

<b>🟡 با استفاده از دستور زیر کد 5 رقمی ارسال شده ب اکانت رو وارد کنید تا ریموت اکانت رو دریافت کنه :</b>
⚪️ <code>/cod</code> 12345 ⚪️

<b>🟡 درصورتیکه اکانت تایید دو مرحله داشت از دستور زیر استفاده کن و بجای PASSWORD ، رمز رو بزن :</b>
⚪️ <code>/pass</code> PASSWORD ⚪️

<b>🟡 برای دریافت لیست کامل شماره هایی ک توی ریموته از دستور زیر استفاده کن : </b>
⚪️ <code>/list</code> ⚪️

<b>🟡 برای حذف اکانت از دستور زیر استفاده کن :</b>
⚪️ <code>/delacc</code> +989999999999 ⚪️

➖➖➖➖➖➖➖➖➖

<i>⚫️دستورات برای استفاده از ریموت⚫️</i>

🔴 برای ذخیره خشاب ، اول فایل تکست رو ارسال یا فوروارد کن بعدش روش ریپلای بزن و دستور زیر رو بنویس :
🔵 <code>/save</code> 🔵

🔴 برای اضافه کردن کپشن از دستور زیر استفاده کن و بجای Enemy User ، کپشنی ک میخوای رو بزن :
🔵 <code>/cap </code>Enemy User 🔵

🔴 برای حذف کردن کپشن از دستور زیر استفاده کن :
🔵 <code>/delcap</code> 🔵

🔴 برای جوین دادن تمام اکانت ها به گروه از دستور زیر استفاده کت و بجای LINK ، از لینک گپ استفاده کن (اگر گپی ایدی داره ،قبل از ایدیش بجای استفاده از httsp://T.me/ ، از @ استفاده کن) :
🔵 <code>/join</code> LINK 🔵

🔴 برای لفت دادن تمام اکانت ها از گپ از دستور زیر استفاده و بجای ID ، از ایدی عددی گپ استفاده کن :
🔵 <code>/left</code> ID 🔵

🔴 برای تنظیم زمان اسپم به ثانیه از دستور زیر استفاده و بجای 15 از هر عددی ک میخوای استفاده کن (بر حسب ثانیه) :
🔵 <code>/time</code> 15 🔵

🔴 برای ران شدن و کل کردن از دستور زیر استفاده کن و جای ID ، آیدی عددی گپ یا ایدی رباتی ک میخوای توش ران شه استفاده کن :
🔵 <code>/attack</code> ID | USER 🔵

🔴 برای فوروارد پست ، اول پست رو بفرست توی بات و بعد روس ریپلای کن و دستور زیر رو بزن 
🔵 <code>/forward</code> ID postLink 🔵

🔴 برای اتمام ران از دستور زیر استفاده کن :
🔵 <code>/stop</code> 🔵

🔴 برای دریافت کد ورود تلگرام از ریموت از دستور زیر استفاده کن :
🔵 <code>/code</code> +989999999999 🔵

🔴 برای تغییر تگ اکانتا از دستور زیر استفاده کن و بجای Acconut Name ،تگی رو ک میخوای بزن :
🔵 <code>/name</code> Account Name🔵

🔴 برای تنظیم عکس پروفایل اکانتا ، اول عکس رو توی بات بفرست و بعد روش ریپلای کن دستور زیر رو بزن :
🔵 <code>/prof</code> (reply on photo) 🔵

╭━━━━━━━━━━━━━━━➣  
┣⪼❉ <i>Creator</i>
┣⪼❉ <u>Manufacturer channel</u> 
┣⪼❉ <b>@rav_ani</b>
┣⪼❉ <b>Coder AliReza</b> 
┣⪼❉ @Atakeri | @mer_py | @Roh_Bijan
╰━━━━━━━━━━━━━━━➣ ''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.command('list') & filters.user(sudo))
async def getAccountList(client, message):
    accounts = getAccount()
    for session in accounts:
        with open('sessionList.txt', 'a', encoding='utf-8') as file:
            file.write(str(session) + '\n')
    if os.path.isfile('sessionList.txt'):
        await bot.send_document(chat_id=message.chat.id, document='./sessionList.txt', caption='<b>🔅 لیست کل سشن های ربات</b>', reply_to_message_id=message.id)
        os.unlink('sessionList.txt')
    else:
        await message.reply(f'<b>اکانتی یافت نشد !</b>', quote=True)

@bot.on_message(filters.regex('/add ') & filters.user(sudo))
async def sendCode(client, message):
    phone_number = message.text.replace('/add ', '').replace(' ', '').replace('+', '').replace('-', '')
    if os.path.isfile(f'Rimots/{phone_number}.session') :
        await message.reply('<b>شماره مورد نظر از قبل وجود داشت.</b>', quote=True)
    else :
        global login_temp_list
        random_api = app_info()
        login_temp_list['api_id'] = random_api[1]
        login_temp_list['api_hash'] = random_api[0]
        login_temp_list['phone_number'] = phone_number
        login_temp_list['client'] = Client(f'Rimots/{phone_number}', int(login_temp_list['api_id']), login_temp_list['api_hash'])
        try :
            await login_temp_list['client'].connect()
            login_temp_list['response'] = await login_temp_list['client'].send_code(phone_number)
        except errors.BadRequest :
            await message.reply('<b>خطایی رخ داد !</b>', quote=True)
        else:
            await message.reply(f'<b>کد 5 رقمی به شماره {phone_number} ارسال شد ✅</b>', quote=True)


@bot.on_message(filters.regex('/cod ') & filters.user(sudo))
async def setCode(client, message):
    telegram_code = message.text.split()[1].replace(' ', '').replace('-', '')
    global login_temp_list
    if len(login_temp_list.values()) == 0 :
        await message.reply('<b>لطفا ابتدا از دستور sendCode استفاده نمایید.</b>', quote=True)
    else :
        try :
            await login_temp_list['client'].sign_in(login_temp_list['phone_number'], login_temp_list['response'].phone_code_hash, telegram_code)
            await login_temp_list['client'].disconnect()
            login_temp_list = {}
        except errors.SessionPasswordNeeded:
            password_hint = await login_temp_list['client'].get_password_hint()
            await message.reply(f'''اکانت شما دارای تایید دو مرحله ای میباشد.
راهنمای رمز : {password_hint}

لطفا با استفاده از دستور مربوطه رمز تایید دو مرحله را ارسال نمایید.''', quote=True)
        except errors.BadRequest :
            await message.reply('<b>خطایی رخ داد !</b>', quote=True)
        else:
            await message.reply('<b>اکانت با موفقیت اضافه شد ✅</b>', quote=True)


@bot.on_message(filters.regex('/pass ') & filters.user(sudo))
async def set2FA(client, message):
    telegram_2fa_password = message.text.split()[1]
    global login_temp_list
    if len(login_temp_list.values()) == 0 :
        await message.reply('<b>لطفا ابتدا از دستور sendCode استفاده نمایید.</b>', quote=True)
    else :
        try :
            await login_temp_list['client'].check_password(telegram_2fa_password)
        except errors.BadRequest :
            await message.reply('<b>رمز وارد شده اشتباه میباشد, لطفا مجدد تلاش نمایید.</b>', quote=True)
        else:
            await login_temp_list['client'].disconnect()
            login_temp_list = {}
            await message.reply('<b>اکانت با موفقیت اضافه شد ✅</b>', quote=True)


@bot.on_message(filters.regex('/delacc ') & filters.user(sudo))
async def deleteAccount(client, message):
    phone_number = message.text.replace('/delacc ', '').replace(' ', '').replace('+', '').replace('-', '')
    main_path = f'Rimots/{phone_number}.session'
    if not os.path.isfile(main_path) :
        await message.reply('<b>شماره مورد نظر یافت نشد.</b>', quote=True)
    else :
        os.unlink(main_path)
        await message.reply('<b>شماره مورد نظر با موفقیت از ربات حذف شد.</b>', quote=True)


@bot.on_message(filters.command('save') & filters.user(sudo))
async def __SAVE__(client, message) :
    try :
        if message.reply_to_message.document.file_size / 1024 / 1024 <= 5 :
            await bot.download_media(message.reply_to_message.document.file_id, file_name='file.txt')
            await bot.send_message(message.chat.id, '''<b>فایل خشاب ذخیره شد ✅</b>''', reply_to_message_id=message.reply_to_message.id, parse_mode=ParseMode.HTML)
    except :
        await bot.send_message(message.chat.id, '''<b>خطایی رخ داد ❗️</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.regex('/cap ') & filters.user(sudo))
async def __ADD__(client, message) :
    add = message.text.replace('/cap ', '')
    with open('downloads/caption.txt', 'w', encoding="utf-8") as file :
        file.write(add)
    await bot.send_message(message.chat.id, '''<b>جمله مورد نظر به خشاب اضافه شد ✅</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.regex('/time ') & filters.user(sudo))
async def __ADD__(client, message) :
    time = message.text.replace('/time ', '')
    with open('downloads/time.txt', 'w', encoding="utf-8") as file :
        file.write(time)
    await bot.send_message(message.chat.id, '''<b>زمان اسپم با موفقیت تنظیم شد ✅</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.regex('/join ') & filters.user(sudo))
async def __join__(client, message):
    link = message.text.split()[1].replace('@', '').replace('+', 'joinchat/')
    if len(getAccount()) == 0 :
        await bot.send_message(message.from_user.id, f'<b>اکانتی یافت نشد !</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
    else :
        accs = len(getAccount())
        await bot.send_message(message.from_user.id, f'<b>♻️ عملیات عضویت با {accs} اکانت شروع شد ...</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        id = ''
        title = ''
        for session in getAccount() :
            info = app_info()
            try :
                async with Client(f'Rimots/{session}', info[1], info[0]) as cli :
                    await cli.join_chat(link)
                    get_chat = await cli.get_chat(link)
                    title = get_chat.title
                    await bot.send_message(message.from_user.id, f'<b>اکانت [ {session} ] با موفقیت در [ {title} ] عضو شد ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
                    asyncio.run(sleep(1))
            except :
                await bot.send_message(message.from_user.id, f'<b>اکانت [ {session} ] هنگام عضویت با خطا مواجه شد ❗️</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        await bot.send_message(message.from_user.id, f'<b>عملیات جوین با موفقیت به پایان رسید ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.regex('/left ') & filters.user(sudo))
async def __left__(client, message):
    link = message.text.split()[1]
    if len(getAccount()) == 0 :
        await bot.send_message(message.from_user.id, f'<b>اکانتی یافت نشد !</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
    else :
        accs = len(getAccount())
        await bot.send_message(message.from_user.id, f'<b>♻️ عملیات لفت با {accs} اکانت شروع شد ...</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        id = 0
        for session in getAccount() :
            info = app_info()
            try :
                async with Client(f'Rimots/{session}', info[1], info[0]) as cli :
                    get_chat = await cli.get_chat(link)
                    title = get_chat.title
                    await cli.leave_chat(link, delete=True)
                    await bot.send_message(message.from_user.id, f'<b>اکانت [ {session} ] با موفقیت از [ {title} ] خارج شد ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
                    asyncio.run(sleep(1))
            except :
                await bot.send_message(message.from_user.id, f'<b>اکانت [ {session} ] هنگام لفت با خطا مواجه شد ❗️</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        await bot.send_message(message.from_user.id, f'<b>عملیات لفت با موفقیت به پایان رسید ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.regex('/attack ') & filters.user(sudo))
async def __attack__(client, message) :
    link = message.text.split()[1]
    time2sleep = int(open('downloads/time.txt', 'r').read())
    if os.path.exists('stop') :
        os.unlink('stop')
    if os.path.exists('downloads/file.txt') == False :
        await bot.send_message(message.chat.id, '''<b>خشابی یافت نشد ❗️</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
    else :
        await bot.send_message(message.chat.id, '''<b>عملیات اسپم شروع شد ✅</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        with open('downloads/file.txt', 'r', encoding="utf-8") as mf : data = mf.read()
        while True:
            if os.path.exists('stop') :
                break
            for session in getAccount() :
                if os.path.exists('stop') :
                    break
                else:
                    line = ra.choice(data.split('\n')).strip()
                    if os.path.exists('downloads/caption.txt') :
                        with open('downloads/caption.txt', 'r', encoding="utf-8") as tfile :
                            line += '\n\n' + tfile.read()
                    info = app_info()
                    if line == None or len(line) < 2 :
                        continue
                    try :
                        async with Client(f'Rimots/{session}', info[1], info[0]) as cli :
                            await cli.send_message(link, line, parse_mode=ParseMode.HTML)
                        asyncio.run(sleep(time2sleep))
                    except :
                        continue
        await bot.send_message(message.chat.id, f'<b>عملیات اسپم در {link} با موفقیت به پایان رسید ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.regex('/forward ') & filters.user(sudo))
async def __forward__(client, message) :
    link = message.text.split()[1]
    channel = message.text.split()[2].split('/')[3]
    msg_id = int(message.text.split()[2].split('/')[4])
    time2sleep = int(open('downloads/time.txt', 'r').read())
    if os.path.exists('stop') :
        os.unlink('stop')
    await bot.send_message(message.chat.id, '''<b>عملیات اسپم شروع شد ✅</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
    while True:
        if os.path.exists('stop') :
            break
        for session in getAccount() :
            if os.path.exists('stop') :
                break
            else:
                info = app_info()
                try :
                    async with Client(f'Rimots/{session}', info[1], info[0]) as cli :
                        await cli.forward_messages(link, channel, msg_id)
                    asyncio.run(sleep(time2sleep))
                except :
                    continue
    await bot.send_message(message.chat.id, f'<b>عملیات اسپم در {link} با موفقیت به پایان رسید ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)



@bot.on_message(filters.command('stop') & filters.user(sudo))
async def __stop__(client, message) :
    with open('stop', 'w', encoding="utf-8") as file :
        file.write('yes')
    await bot.send_message(message.chat.id, '''<b>تمامی عملیات های ربات با موفقیت کنسل شد ✅</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.command('delcap') & filters.user(sudo))
async def __stop__(client, message) :
    if os.path.exists('downloads/caption.txt') :
        os.unlink('downloads/caption.txt')
    await bot.send_message(message.chat.id, '''<b>کپشن با موفقیت حذف شد ✅</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.regex('/code ') & filters.user(sudo))
async def __code__(client, message):
    number = message.text.split()[1].replace(' ', '').replace('+', '')
    if not os.path.exists(f'Rimots/{number}.session') :
        await bot.send_message(message.from_user.id, '''<b>شماره مورد نظر وجود ندارد.</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
    else :
        try :
            info = app_info()
            async with Client(f'Rimots/{number}', info[1], info[0]) as cli :
                text = await cli.get_history(777000, limit=1)[0]['text']
                if text :
                    await bot.send_message(message.from_user.id, text, reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
                else :
                    await bot.send_message(message.from_user.id, '''پیامی از طرف تلگرام یافت نشد !''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        except :
            await bot.send_message(message.from_user.id, '''<b>هنگام فراخوانی سشن خطایی رخ داد ❗️</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.regex('/name ') & filters.user(sudo))
async def __name__(client, message):
    name = message.text.replace('/name ', '')
    if len(getAccount()) == 0 :
        await bot.send_message(message.from_user.id, f'<b>اکانتی یافت نشد !</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
    else :
        accs = len(getAccount())
        await bot.send_message(message.from_user.id, f'<b>♻️ عملیات تغییر نام پروفایل با {accs} اکانت شروع شد ...</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        for session in getAccount() :
            info = app_info()
            try :
                async with Client(f'Rimots/{session}', info[1], info[0]) as cli :
                    await cli.update_profile(first_name=name, last_name="")
                    await bot.send_message(message.from_user.id, f'<b>نام پروفایل اکانت [ {session} ] با موفقیت به [ {name} ] تغییر یافت ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
                    asyncio.run(sleep(1))
            except :
                await bot.send_message(message.from_user.id, f'<b>اکانت [ {session} ] هنگام تغییر نام با خطا مواجه شد ❗️</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        await bot.send_message(message.from_user.id, f'<b>عملیات تغییر نام با موفقیت به پایان رسید ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


@bot.on_message(filters.command('profile') & filters.user(sudo))
async def __profile__(client, message) :
    if len(getAccount()) == 0 :
        await bot.send_message(message.from_user.id, f'<b>اکانتی یافت نشد !</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
    else :
        try :
            await bot.download_media(message.reply_to_message.photo.file_id, file_name='photo.png')
        except :
            await bot.send_message(message.chat.id, '''<b>خطایی رخ داد ❗️</b>''', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
        if os.path.exists('downloads/photo.png') :
            accs = len(getAccount())
            await bot.send_message(message.from_user.id, f'<b>♻️ عملیات تغییر عکس پروفایل با {accs} اکانت شروع شد ...</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
            for session in getAccount() :
                info = app_info()
                try :
                    async with Client(f'Rimots/{session}', info[1], info[0]) as cli :
                        await cli.set_profile_photo(photo='downloads/photo.png')
                        await bot.send_message(message.from_user.id, f'<b>عکس پروفایل اکانت [ {session} ] با موفقیت تغییر یافت ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
                        asyncio.run(sleep(1))
                except :
                    await bot.send_message(message.from_user.id, f'<b>اکانت [ {session} ] هنگام تغییر عکس پروفایل با خطا مواجه شد ❗️</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)
            os.unlink('downloads/photo.png')
            await bot.send_message(message.from_user.id, f'<b>عملیات تغییر عکس پروفایل با موفقیت به پایان رسید ✅</b>', reply_to_message_id=message.id, parse_mode=ParseMode.HTML)


bot.run()
