from SimpleQIWI import *
from pyqiwip2p import QiwiP2P
import random
from aiogram.utils.markdown import hlink
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import but
TOKEN = " TOKEN "

button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
button_hi2 = KeyboardButton('💵Пополнить💵')
button_hi3 = KeyboardButton('💸Вывод💸')
button_hi4 = KeyboardButton('📈Краш📈')
button_hi5 = KeyboardButton('🎰Рулетка🎰')
button_hi6 = KeyboardButton('🎲Кости🎲')
pom = KeyboardButton('Тех. поддержка📑')
qiwi = KeyboardButton('Киви🥝')
card = KeyboardButton('Карта💳')
button_prov = KeyboardButton('💵Проверить💵')

dice1 = KeyboardButton('1')
dice2 = KeyboardButton('2')
dice3 = KeyboardButton('3')
dice4 = KeyboardButton('4')
dice5 = KeyboardButton('5')
dice6 = KeyboardButton('6')
dice1_3 = KeyboardButton('1-3')
dice4_6 = KeyboardButton('4-6')
dice1_2 = KeyboardButton('1-2')
dice3_4 = KeyboardButton('3-4')
dice5_6 = KeyboardButton('5-6')

play = KeyboardButton("Играть🎮")

pr = ReplyKeyboardMarkup(resize_keyboard=True).add(button_prov).add(button_hi)
global p2p
p2p = QiwiP2P(auth_key='eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjVzNnhodC0wMCIsInVzZXJfaWQiOiI3OTUyOTM5MzI5OSIsInNlY3JldCI6ImU1NmQ3Nzc1OTZjY2QyNmRjY2YzOGM0N2NjNjk3YTFjMTMxYTNiZWM1NTNiNzE4ZTlmZDA5OWMyYWYxMGQxNGIifX0=')
global kv
kv = ReplyKeyboardMarkup(resize_keyboard=True).add(play).add(button_hi)
global gr
gr = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi).row(button_hi2,button_hi3).row(button_hi4,button_hi5,button_hi6).add(pom).add(qiwi, card)
global dice
dice = ReplyKeyboardMarkup(resize_keyboard=True).row(dice1_3, dice4_6).row(dice1_2,dice3_4,dice5_6).row(dice1,dice2,dice3,dice4,dice5,dice6).add(button_hi)

db = sqlite3.connect('account.db')
sql = db.cursor()

token = "e34362c1d0f1413097f05596053a56ff"
phone = "+79513747922"

def find(idbv, num:int):
    resul = sql.execute(f"Select * from users where userid = ({idbv})")
    resu = resul.fetchone()[num]
    return resu

api = QApi(token=token, phone=phone)

sql.execute("""CREATE TABLE IF NOT EXISTS users (
        userid INT,
        username TEXT,
        donat INT,
        activ INT,
        bonus INT,
        qiwi INT,
        card INT,
        poym INT
    )""")
db.commit()
stor = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=stor)

class Form(StatesGroup):
    st = State()
    gm = State()
    kr = State()
    gk = State()
    sy = State()
    po = State()
    rul = State()
    rulst = State()
    popb = State()
    obn = State()
    vip = State()
    qiwin = State()
    cardn = State()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    
    id = message.from_user.id
    name = message.from_user.full_name
    sql.execute(f"Select userid from users where userid = {id}")
    data = sql.fetchone()
    if data is None:
        sql.execute("insert into users values (?, ?, ?, ?, ?, ?, ?, ?);", (id, name, 0, 0, 1, 0, 0, 0))
        db.commit() 
    res = sql.execute(f"Select * from users where userid = ({id})")
    idus = res.fetchone()[2]
    res1 = sql.execute(f"Select * from users where userid = ({id})")
    pok = res1.fetchone()[3]
    res2 = sql.execute(f"Select * from users where userid = ({id})")
    pok1 = res2.fetchone()[4]
    viv = find(id,7)
    car = "Карта💳"
    qiw = "QiWi🥝"
    if pok1 == 1:
        if viv == 0:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: Не выбран⚠️\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
        if viv == 1:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {qiw}\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
        if viv == 2:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {car}\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
    if pok1 == 0:
        if viv == 0:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: Не выбран⚠️\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)
        if viv == 1:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {qiw}\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)
        if viv == 2:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {car}\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)

@dp.message_handler(text="🙍‍♂️Личный кабинет🙍‍♂️")
async def with_puree(message: types.Message):
    id = message.from_user.id
    name = message.from_user.full_name
    sql.execute(f"Select userid from users where userid = {id}")
    data = sql.fetchone()
    if data is None:
        sql.execute("insert into users values (?, ?, ?, ?, ?, ?, ?, ?);", (id, name, 0, 0, 1, 0, 0, 0))
        db.commit()
    res = sql.execute(f"Select * from users where userid = ({id})")
    idus = res.fetchone()[2]
    res1 = sql.execute(f"Select * from users where userid = ({id})")
    pok = res1.fetchone()[3]
    res2 = sql.execute(f"Select * from users where userid = ({id})")
    pok1 = res2.fetchone()[4]
    viv = find(id,7)
    car = "Карта💳"
    qiw = "QiWi🥝"
    if pok1 == 1:
        if viv == 0:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: Не выбран⚠️\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
        if viv == 1:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {qiw}\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
        if viv == 2:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {car}\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
    if pok1 == 0:
        if viv == 0:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: Не выбран⚠️\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)
        if viv == 1:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {qiw}\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)
        if viv == 2:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {car}\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)

@dp.message_handler(text="🙍‍♂️Личный кабинет🙍‍♂️", state="*")
async def with_puree(message: types.Message, state: FSMContext ):
    if state is None:
        return
    await state.finish()
    id = message.from_user.id
    name = message.from_user.full_name
    res = sql.execute(f"Select * from users where userid = ({id})")
    idus = res.fetchone()[2]
    res1 = sql.execute(f"Select * from users where userid = ({id})")
    pok = res1.fetchone()[3]
    res2 = sql.execute(f"Select * from users where userid = ({id})")
    pok1 = res2.fetchone()[4]
    viv = find(id,7)
    car = "Карта💳"
    qiw = "QiWi🥝"
    if pok1 == 1:
        if viv == 0:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: Не выбран⚠️\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
        if viv == 1:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {qiw}\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
        if viv == 2:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {car}\nВаше количество выводов: {pok}💰\nБонус: доступен🎁", reply_markup=but.keyb)
    if pok1 == 0:
        if viv == 0:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: Не выбран⚠️\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)
        if viv == 1:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {qiw}\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)
        if viv == 2:
            await bot.send_message(id, f"Личный кабинет, {name}!🤚\nВаш ID: {id}🔥\nВаш баланс: {idus}₽💸\nВывод: {car}\nВаше количество выводов: {pok}💰\nБонус: недоступен🎁", reply_markup=gr)

@dp.message_handler(text="Бонус🎁")
async def with_puree(message: types.Message):
    id = message.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    idus = res.fetchone()[2]
    bon = find(id, 4)
    if bon == 1:
        await message.answer("Бонус получен🎉\nЗачисленно - 25₽💸")
        boni = idus + 25
        sqlbon(id, 0)
        sqlup(id, boni)

@dp.message_handler(text="🎰Рулетка🎰")
async def with_puree(message: types.Message):
    id = message.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    global idus 
    idus = res.fetchone()[2] 
    st1 = KeyboardButton(50) 
    st2 = KeyboardButton(100) 
    cb = idus//2 
    st3 = KeyboardButton(cb) 
    st4 = KeyboardButton(idus) 
    sta = ReplyKeyboardMarkup(resize_keyboard=True).row(st1,st2,st3,st4).add(button_hi) 
    await message.answer(f"Ваш баланс: {idus}₽\nМинимальная ставка: 50₽!\nЧтобы указать свою ставку,\nВведите число:", reply_markup=sta) 
    await Form.rulst.set()

@dp.message_handler(text = "🎲Кости🎲") 
async def dice_start(message: types.Message) -> None: 
    id = message.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    global idus 
    idus = res.fetchone()[2] 
    st1 = KeyboardButton(50) 
    st2 = KeyboardButton(100) 
    cb = idus//2 
    st3 = KeyboardButton(cb) 
    st4 = KeyboardButton(idus) 
    sta = ReplyKeyboardMarkup(resize_keyboard=True).row(st1,st2,st3,st4).add(button_hi) 
    await message.answer(f"Ваш баланс: {idus}₽\nМинимальная ставка: 50₽!\nЧтобы указать свою ставку\nВведите число:", reply_markup=sta) 
    await Form.st.set()

@dp.message_handler(text = "Киви🥝") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id
    bra = find(id, 5)
    if bra == 0:
        button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
        key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
        await message.answer(f'У вас не указаны реквизиты кошелька⚠️\nНапишите номер кошелька: (Пример: 7xxxxxxxxxx)', reply_markup=key)
        await Form.qiwin.set()
    if bra != 0:
        button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
        izm = KeyboardButton('Изменить📝')
        izm1 = KeyboardButton('По умолчанию📌')
        key = ReplyKeyboardMarkup(resize_keyboard=True).add(izm).add(izm1).add(button_hi)
        await message.answer(f'Указан кошелёк: +{bra} ✅\nЧтобы изменить - "Изменить📝"\nИли введите новый кошелёк⚠️', reply_markup=key)
        await Form.qiwin.set()

@dp.message_handler(text = "Карта💳") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id
    bra = find(id, 6)
    if bra == 0:
        button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
        key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
        await message.answer(f'У вас не указаны реквизиты карты⚠️\nНапишите номер карты: (Пример: 4652607212050005)', reply_markup=key)
        await Form.cardn.set()
    if bra != 0:
        button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
        izm = KeyboardButton('Изменить📝')
        izm1 = KeyboardButton('По умолчанию📌')
        key = ReplyKeyboardMarkup(resize_keyboard=True).add(izm).add(izm1).add(button_hi)
        await message.answer(f'Указан номер карты: {bra} ✅\nЧтобы изменить - "Изменить📝"\nИли введите новую карту⚠️', reply_markup=key)
        await Form.cardn.set()

@dp.message_handler(content_types=['text'], state=Form.cardn) 
async def krash_game(msg:types.Message, state: FSMContext) -> None:
    id = msg.from_user.id
    bra = find(id, 5)
    if msg.text == "Изменить📝":
        if bra == 0:
            await msg.answer(f'Сначало введите реквизиты карты⚠️')
            await state.finish()
        if bra != 0:
            await msg.answer(f'Напишите новый номер в сообщении:\n(Пример: 4652607212050005)')
    if msg.text == "По умолчанию📌":
        button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
        key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
        await msg.answer('Карта выбрана по умолчанию✅', reply_markup=key)
        cardm(id)
        await state.finish()
    try:
        nor = int(msg.text)
        did = len(str(msg.text))
        if did == 16:
            await msg.answer(f'Успешно✅\nВаш номер карты: {msg.text} 🎉')
            sqlcard(id, nor)
            await state.finish()
        if did != 16:
            await msg.answer(f'Слишком маленький номер⚠️')
    except:
        if msg.text != "Изменить📝" and msg.text != "По умолчанию📌":
            await msg.answer(f'Введите номер⚠️ (Пример: 4652607212050005) ')

@dp.message_handler(content_types=['text'], state=Form.qiwin) 
async def krash_game(msg:types.Message, state: FSMContext) -> None:
    id = msg.from_user.id
    bra = find(id, 5)
    if msg.text == "Изменить📝":
        if bra == 0:
            await msg.answer(f'Введите реквизиты кошелька⚠️')
            await state.finish()
        if bra != 0:
            await msg.answer(f'Напишите новые реквизиты в сообщении⚠️\n(Пример: 7xxxxxxxxxx)')
    if msg.text == "По умолчанию📌":
        button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
        key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
        await msg.answer('QiWi выбран по умолчанию✅', reply_markup=key)
        qiwim(id)
        await state.finish()
    try:
        nor = int(msg.text)
        nor1 = str(msg.text)
        did = len(str(msg.text))
        if "7" in nor1[0]:
            if did == 11:
                await msg.answer(f'Успешно✅\nВаш киви номер: +{msg.text} 🎉')
                sqlqiwi(id, nor)
                await state.finish()
            if did != 11:
                await msg.answer(f'⚠️Слишком маленький или большой номер⚠️')
        else:
            await msg.answer('⚠️Номер должен начинаться с 7')
    except:
        if msg.text != "Изменить📝" and msg.text != "По умолчанию📌":
            await msg.answer(f'Введите номер⚠️')


@dp.message_handler(text = "📈Краш📈") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    global idus 
    idus = res.fetchone()[2] 
    st1 = KeyboardButton(50) 
    st2 = KeyboardButton(100) 
    cb = idus//2 
    st3 = KeyboardButton(cb) 
    st4 = KeyboardButton(idus) 
    sta = ReplyKeyboardMarkup(resize_keyboard=True).row(st1,st2,st3,st4).add(button_hi) 
    await message.answer(f"Ваш баланс: {idus}₽\nМинимальная ставка: 50₽!\nЧтобы указать свою ставку\nВведите число:", reply_markup=sta) 
    await Form.kr.set()

@dp.message_handler(text = "💸Вывод💸") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id
    res = sql.execute(f"Select * from users where userid = ({id})")
    idus = res.fetchone()[2]
    uiu = find(id, 7)
    if uiu != 0:
        if idus <= 49:
            await message.answer('Недостаточно денег для вывода⚠️\nМин. количество для вывода - 50₽')
        if idus >= 50:
            await bot.send_message(id,f'Доступно {idus}₽ для вывода✅\nМин. количество для вывода: 50₽\nМакс. количество для вывода: 5000₽\nВведите количество которое хотите снять:')
            await Form.vip.set()
    if uiu == 0:
        await message.answer('Выберите способ вывода⚠️')


@dp.message_handler(text = "Тех. поддержка📑") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id 
    await message.answer('По всем вопросам обрашаться\nВ тех. поддержку - @tehpodderzca')

@dp.message_handler(text = "поп") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id 
    if id == 1028676957:
        await message.answer('ID:')
        await Form.popb.set()

@dp.message_handler(text = "обн") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id
    if id == 1028676957:
        await message.answer('ID:')
        await Form.obn.set()

@dp.message_handler(text = "бал") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id 
    if id == 1028676957:
        await message.answer(f'Баланс на киви: {api.balance[0]}')
        
@dp.message_handler(content_types=['text'], state=Form.popb) 
async def krash_game(msg:types.Message, state: FSMContext) -> None:
    try:
        bb = int(msg.text) 
        sqlup(bb, 10000)
        await state.finish()
        await msg.answer('Успешно!')
    except:
        await msg.answer('Пошёл нахуй, гандон')

@dp.message_handler(content_types=['text'], state=Form.obn) 
async def krash_game(msg:types.Message, state: FSMContext) -> None:
    try:
        bb = int(msg.text)
        sqlup(bb, 0)
        await state.finish()
        await msg.answer('Успешно!')
    except:
        await msg.answer('Пошёл нахуй, гандон')

@dp.message_handler(text = "💵Пополнить💵") 
async def crash_start(message: types.Message) -> None: 
    id = message.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    global idus 
    idus = res.fetchone()[2] 
    st1 = KeyboardButton(50) 
    st2 = KeyboardButton(100)
    st3 = KeyboardButton(150) 
    st4 = KeyboardButton(200) 
    sta = ReplyKeyboardMarkup(resize_keyboard=True).row(st1,st2,st3,st4).add(button_hi) 
    await message.answer(f"Ваш баланс: {idus}₽\nМин. количество - 50₽\nУказать сумму пополнения\nВведите в чат число:", reply_markup=sta) 
    await Form.sy.set()

@dp.message_handler(content_types=['text'], state=Form.vip) 
async def krash_game(msg:types.Message, state: FSMContext) -> None:
    id = msg.from_user.id
    gh = find(id, 5)
    carde = find(id, 6)
    if carde != 0 or gh != 0:
            dat = int(msg.text)
            id = msg.from_user.id
            res = sql.execute(f"Select * from users where userid = ({id})")
            idus = res.fetchone()[2]
            res1 = sql.execute(f"Select * from users where userid = ({id})")
            pok = res1.fetchone()[3]
            if dat <= 5000 and dat >= 50:
                if dat <= idus:
                    await msg.answer('Заявка успешно принята✅\nОплата будет совершена в течении 5 рабочих дней⚠️')
                    vbn = idus - dat
                    sqlup(id, vbn)
                    nmm = pok + 1
                    sqlac(id, nmm)
                    bnm = find(id, 7)
                    cardf = find(id, 6)
                    qiwif = find(id, 5)
                    if bnm == 1:
                        await bot.send_message(1028676957, f'Заявка на {dat}₽\nОт пользователя с ID: {id}')
                        await bot.send_message(1028676957, f'{qiwif}')
                        await state.finish()
                    if bnm == 2:
                        await bot.send_message(1028676957, f'Заявка на {dat}₽\nОт пользователя с ID: {id}')
                        await bot.send_message(1028676957, f'{cardf}')
                        await state.finish()
                else:
                    await msg.answer(f'Вы превысили свой баланс⚠️')
            else:
                await msg.answer(f'Мин. количество для вывода: 50₽\nМакс. количество для вывода: 5000₽')
    else:
        await msg.answer('Укажите ревезиты в личном кабинете⚠️')
        await state.finish()

@dp.message_handler(content_types=['text'], state=Form.st) 
async def dice_game(msg:types.Message, state: FSMContext) -> None: 
    try:
        id = msg.from_user.id 
        res = sql.execute(f"Select * from users where userid = ({id})") 
        idus = res.fetchone()[2]
        global ld
        ld = msg.text
        bb = int(msg.text) 
        if bb >= 50 and bb <= idus:
            await msg.answer(f'Ваш баланс: {idus}₽\nВаша ставка: {bb}₽\n1-3, 4-6 - X2️⃣!\n1-2, 3-4, 5-6 - X3️⃣!!\n1, 2, 3, 4, 5, 6 - X6️⃣!!!',reply_markup=dice) 
            await Form.gm.set() 
        if bb <= 49: 
            bb = f"Минимальная ставка - 50₽⚠️" 
            await msg.answer(bb) 
            await state.finish()
        if bb > idus: 
            bb = f"Вы ввели ставку превышающую ваш баланс⚠️" 
            await msg.answer(bb) 
            await state.finish() 
    except:
        await msg.answer("Введите только число⚠️") 

@dp.message_handler(content_types=['text'], state=Form.rulst) 
async def krash_game(msg:types.Message, state: FSMContext) -> None:

        global bb
        bb = int(msg.text) 
        if type(bb) == int or float:
            id = msg.from_user.id 
            res = sql.execute(f"Select * from users where userid = ({id})") 
            idus = res.fetchone()[2]
            global ld
            ld = msg.text
            bb = int(msg.text) 
            if bb >= 50 and bb <= idus:
                await msg.answer(f'Ваш баланс: {idus}₽\nВаша ставка: {bb}₽\nВыпадает коффицент, который умножает ваш баланс🎉',reply_markup=but.rul) 
                await Form.rul.set() 
            if bb <= 49: 
                bb = f"Минимальная ставка - 50₽⚠️" 
                await msg.answer(bb) 
                await state.finish()
            if bb > idus: 
                bb = f"Вы ввели ставку превышающую ваш баланс⚠️" 
                await msg.answer(bb) 
                await state.finish()
        if type(bb) == str: 
            bb = f"Введите только число⚠️" 

@dp.message_handler(content_types=['text'], state=Form.kr) 
async def krash_game(msg:types.Message, state: FSMContext) -> None:

        global bb
        bb = int(msg.text) 
        if type(bb) == int or float:
            id = msg.from_user.id 
            res = sql.execute(f"Select * from users where userid = ({id})") 
            idus = res.fetchone()[2]
            global ld
            ld = msg.text
            bb = int(msg.text) 
            if bb >= 50 and bb <= idus:
                await msg.answer(f'Ваш баланс: {idus}₽\nВаша ставка: {bb}₽\nВыпадает коффицент, который умножает ваш баланс🎉',reply_markup=kv) 
                await Form.gk.set() 
            if bb <= 49: 
                bb = f"Минимальная ставка - 50₽⚠️" 
                await msg.answer(bb) 
                await state.finish()
            if bb > idus: 
                bb = f"Вы ввели ставку превышающую ваш баланс⚠️" 
                await msg.answer(bb) 
                await state.finish()
        if type(bb) == str: 
            bb = f"Введите только число⚠️" 
            await msg.answer(bb)

@dp.message_handler(content_types=['text'], state=Form.sy) 
async def krash_game(msg:types.Message, state: FSMContext) -> None:

        global bb
        bb = int(msg.text) 
        if type(bb) == int or float:
            id = msg.from_user.id 
            res = sql.execute(f"Select * from users where userid = ({id})") 
            idus = res.fetchone()[2]
            global ld
            ld = msg.text
            global bbbn
            bbbn = int(msg.text)
            global price
            price = bbbn
            global comm
            if bbbn >= 50:
                com = (f'{id}' + '_' + str(random.randint(1,99999)))
                comm = p2p.bill(amount=bbbn, lifetime=15, comment=com)
                text = hlink(f'Ссылка', '{comm}')
                await msg.answer(f'Ссылка для оплаты: {comm.pay_url}', reply_markup=pr)
                await Form.po.set()
            if bbbn <= 49:
                await msg.answer('Мин. количество для пополнения - 50₽⚠️')
        if type(bbbn) == str: 
            bbbn = f"Введите только число⚠️" 
            await msg.answer(bb)

def sqlup(id, value):
    sql.execute(f"update users set donat = {value} where userid = {id}")
    db.commit()

def sqlac(id, value):
    sql.execute(f"update users set activ = {value} where userid = {id}")
    db.commit()

def sqlqiwi(id, value):
    sql.execute(f"update users set qiwi = {value} where userid = {id}")
    db.commit()

def sqlcard(id, value):
    sql.execute(f"update users set card = {value} where userid = {id}")
    db.commit()

def sqlbon(id, value):
    sql.execute(f"update users set bonus = {value} where userid = {id}")
    db.commit()

def cardm(id):
    sql.execute(f"update users set poym = 2 where userid = {id}")
    db.commit()

def qiwim(id):
    sql.execute(f"update users set poym = 1 where userid = {id}")
    db.commit()

@dp.message_handler(content_types=['text'], state=Form.po) 
async def dice_start(msg:types.Message, state: FSMContext) -> None:
    id = msg.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    idus = res.fetchone()[2]
    if msg.text == "💵Проверить💵":
        bt = p2p.check(bill_id=comm).status
        if str(bt) == "PAID":
            button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
            bnm = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
            await msg.answer(f'Успешно✅', reply_markup=bnm)
            mn = idus + bbbn
            sqlup(id, mn)
            await bot.send_message(5225100069, f'Теперь баланс на киви: {api.balance[0]}')
            await state.finish()
        else:  
            await msg.answer(f'⚠️Ожидаю оплату⚠️ Ссылка для оплаты: {comm.pay_url}')



@dp.message_handler(content_types=['text'], state=Form.rul) 
async def rul_start(msg:types.Message, state: FSMContext) -> None:
    bn = random.randint(1,100)
    id = msg.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    idus = res.fetchone()[2]
    g = random.choice(but.lists)
    r = int(ld)
    v = int(idus)
    if v >= r:
        print(g)
        if msg.text == g:
            await msg.answer(f'Ставка умножена на: x36🎉🎉🎉\nВаш баланс: {v}₽\nВаша ставка: {r}\nВыпало: {g}')
            win = idus - r
            wi = r * 36 + v
            sqlup(id, round(wi))
        if msg.text == "Red🟥":
            if g in but.listr:
                await msg.answer(f'Ставка умножена на: x2🎉\nВаш баланс: {v}₽\nВаша ставка: {r}\nВыпало: {g}')
                winw = idus + r
                sqlup(id, round(winw))
            if g not in but.listr:
                await msg.answer(f'Проигрыш! Выпало - {g}\nВаш баланс: {v}₽\nВаша ставка: {r}')
                win = idus - r
                sqlup(id, round(win))
        if msg.text == "Black⬛":
            if g not in but.listr:
                await msg.answer(f'Ставка умножена на: x2🎉\nВаш баланс: {v}₽\nВаша ставка: {r}\nВыпало: {g}')
                winw = idus + r
                sqlup(id, round(winw))
            if g in but.listr:
                await msg.answer(f'Проигрыш! Выпало - {g}\nВаш баланс: {v}₽\nВаша ставка: {r}')
                win = idus - r
                sqlup(id, round(win))
        if msg.text == "1st 12":
            if g in but.st121:
                await msg.answer(f'Ставка умножена на: x3🎉\nВаш баланс: {v}₽\nВаша ставка: {r}\nВыпало: {g}')
                winw = idus + 2 * r
                sqlup(id, round(winw))
            if g not in but.st121:
                await msg.answer(f'Проигрыш! Выпало - {g}\nВаш баланс: {v}₽\nВаша ставка: {r}')
                win = idus - r
                sqlup(id, round(win))
        if msg.text == "2nd 12":
            if g in but.nd12:
                await msg.answer(f'Ставка умножена на: x3🎉\nВаш баланс: {v}₽\nВаша ставка: {r}\nВыпало: {g}')
                winw = idus + 2 * r
                sqlup(id, round(winw))
            if g not in but.nd12:
                await msg.answer(f'Проигрыш! Выпало - {g}\nВаш баланс: {v}₽\nВаша ставка: {r}')
                win = idus - r
                sqlup(id, round(win))
        if msg.text == "3rd 12":
            if g in but.rd12:
                await msg.answer(f'Ставка умножена на: x3🎉\nВаш баланс: {v}₽\nВаша ставка: {r}\nВыпало: {g}')
                winw = idus + 2 * r
                sqlup(id, round(winw))
            if g not in but.rd12:
                await msg.answer(f'Проигрыш! Выпало - {g}\nВаш баланс: {v}₽\nВаша ставка: {r}')
                win = idus - r
                sqlup(id, round(win))
        if msg.text == "1 to 18":
            if g in but.to18:
                await msg.answer(f'Ставка умножена на: x2🎉\nВаш баланс: {v}₽\nВаша ставка: {r}\nВыпало: {g}')
                winw = idus + r
                sqlup(id, round(winw))
            if g not in but.to18:
                await msg.answer(f'Проигрыш! Выпало - {g}\nВаш баланс: {v}₽\nВаша ставка: {r}')
                win = idus - r
                sqlup(id, round(win))
        if msg.text == "19 to 36":
            if g in but.to36:
                await msg.answer(f'Ставка умножена на: x2🎉\nВаш баланс: {v}₽\nВаша ставка: {r}\nВыпало: {g}')
                winw = idus + r
                sqlup(id, round(winw))
            if g not in but.to36:
                await msg.answer(f'Проигрыш! Выпало - {g}\nВаш баланс: {v}₽\nВаша ставка: {r}')
                win = idus - r
                sqlup(id, round(win))
        if msg.text != g and msg.text != "Black⬛" and msg.text != "Red🟥" and msg.text != "1st 12" and msg.text != "2nd 12" and msg.text != "3rd 12" and msg.text != "1 to 18" and msg.text != "19 to 36":
            await msg.answer(f'Проигрыш!\nВаш баланс: {v}₽\nВаша ставка: {r}')
            win = idus - r
            sqlup(id, round(win))
    else:
        await msg.answer(f"Недостаточно денег⚠️\nБаланс: {idus}₽")

@dp.message_handler(content_types=['text'], state=Form.gk) 
async def dice_start(msg:types.Message, state: FSMContext) -> None:
    bn = random.randint(1,100)
    global nb
    if bn >= 0 and bn<= 10:
        lis01 = ['1x', '1.5x', '2x', '3x']
        
        nb = random.choice(lis01)
        print(bn)
    if bn >= 11 and bn<= 40:
        lis14 = ['0.5x', '0.75x', '1x', '1.25x', '1.5x']
        nb = random.choice(lis14)
        print(bn)
    if bn >= 41 and bn <= 100:
        lis41 = ['0x', '0.5x', '0.75x', '1x']
        nb = random.choice(lis41)
        print(bn)
    lis = ['0x', '0.5x', '0.75x', '1x', '2x', '5x']
    id = msg.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    idus = res.fetchone()[2]
    g = random.choice(lis)
    r = int(ld)
    v = int(idus)
    if v >= r:
        if nb == '0x':
            await msg.answer(f'Ставка умножена на: {nb}🎉\nВаш баланс: {v}₽\nВаша ставка: {r} ')
            win = idus - r
            sqlup(id, round(win))
        if nb == '0.5x':
            await msg.answer(f'Ставка умножена на: {nb}🎉\nВаш баланс: {v}₽\nВаша ставка: {r} ')
            win = idus - r * 0.5
            sqlup(id, round(win))
        if nb == '0.75x':
            await msg.answer(f'Ставка умножена на: {nb}🎉\nВаш баланс: {v}₽\nВаша ставка: {r} ')
            win = idus - r * 0.75
            sqlup(id, round(win))
        if nb == '1x':
            await msg.answer(f'Ставка умножена на: {nb}🎉\nВаш баланс: {v}₽\nВаша ставка: {r} ')
        if nb == '1.25x':
            await msg.answer(f'Ставка умножена на: {nb}🎉\nВаш баланс: {v}₽\nВаша ставка: {r} ')
            win = idus + r * 1.25
            sqlup(id, round(win))
        if nb == '1.5x':
            await msg.answer(f'Ставка умножена на: {nb}🎉\nВаш баланс: {v}₽\nВаша ставка: {r} ')
            win = idus + r * 1.5
            sqlup(id, round(win))
        if nb == '2x':
            await msg.answer(f'Ставка умножена на: {nb}🎉\nВаш баланс: {v}₽\nВаша ставка: {r} ')
            win = idus + r * 2
            sqlup(id, round(win))
        if nb == '3x':
            await msg.answer(f'Ставка умножена на: {nb}🎉\nВаш баланс: {v}₽\nВаша ставка: {r} ')
            win = idus + r * 3
            sqlup(id, round(win))
    else:
        await msg.answer(f"Недостаточно денег⚠️\nБаланс: {idus}₽")
    

@dp.message_handler(content_types=['text'], state=Form.gm) 
async def dice_start(msg:types.Message, state: FSMContext) -> None: 
    lis = ['1', '2', '3', '4', '5', '6']
    id = msg.from_user.id 
    res = sql.execute(f"Select * from users where userid = ({id})") 
    idus = res.fetchone()[2]
    g = random.choice(lis)
    b = random.choice(lis)
    r = int(ld)
    v = int(idus)
    _6x = r * 6 + idus
    _3x = r * 3 + idus
    _2x = r * 2 + idus
    lose = v - r
    if v >= r:
        if msg.text == '1':
            if g == '1':
                sqlup(id, _6x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)

            else:
                
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
                
        if msg.text == '2':
            if g == '2':
                sqlup(id, _6x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '3':
            if g == '3':
                sqlup(id, _6x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '4':
            sqlup(id, _6x)
            if g == '4':
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '5':
            if g == '5':
                sqlup(id, _6x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '6':
            if g == '6':
                sqlup(id, _6x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '1-2':
            if g == '1' or g == '2':
                sqlup(id, _3x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '3-4':
            if g == '3' or g == '4':
                sqlup(id, _3x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '5-6':
            if g == '5' or g == '6':
                sqlup(id, _3x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '1-3':
            if g == '1' or g == '2' or g == '3':
                sqlup(id, _2x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
        if msg.text == '4-6':
            if g == '4' or g == '5' or g == '6':
                sqlup(id, _2x)
                await msg.answer(f'🎉Выйгрыш🎉\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
            else:
                sqlup(id, lose)
                await msg.answer(f'Проигрыш⚠️\nВыпало число: {g}\nВаш баланс: {idus}₽\nВаша ставка: {ld}₽\n', reply_markup=dice)
    else:
        await msg.answer(f'Недостаточно денег⚠️\nБаланс: {idus}₽')

executor.start_polling(dp)
