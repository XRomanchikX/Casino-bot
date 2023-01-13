from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
            #0

lists = ['0🟩','1🟥','2⬛','3🟥','4⬛','5🟥','6⬛','7🟥','8⬛','9🟥','10⬛','11⬛','12🟥','13⬛','14🟥','15⬛','16🟥','17⬛','18🟥','19🟥','20⬛','21🟥','22⬛','23🟥','24⬛','25🟥','26⬛','27🟥','28⬛','29⬛','30🟥','31⬛','32🟥','33⬛','34🟥','35⬛','36🟥']
listr = ['1🟥', '3🟥','5🟥','7🟥','9🟥','12🟥','14🟥','16🟥','18🟥','19🟥','21🟥','23🟥','25🟥','27🟥','30🟥','32🟥','34🟥','36🟥']
st121 = ['1🟥','3🟥','5🟥','7🟥','9🟥','12🟥','2⬛','4⬛','6⬛','8⬛','10⬛','11⬛']
nd12 = ['14🟥', '16🟥','18🟥','19🟥','21🟥','23🟥','13⬛','15⬛','17⬛','20⬛','22⬛','24⬛']
rd12 = ['25🟥','27🟥','30🟥','32🟥','34🟥','36🟥','26⬛','29⬛','28⬛','31⬛','33⬛','35⬛']
to18 = ['1🟥','3🟥','5🟥','7🟥','9🟥','12🟥','14🟥', '16🟥','18🟥','2⬛','4⬛','6⬛','8⬛','10⬛','11⬛','13⬛','15⬛','17⬛']
to36 = ['19🟥','21🟥','23🟥','20⬛','22⬛','24⬛','25🟥','27🟥','30🟥','32🟥','34🟥','36🟥','26⬛','29⬛','28⬛','31⬛','33⬛','35⬛']
st0 = KeyboardButton('0🟩')
st1 = KeyboardButton('1🟥')
st2 = KeyboardButton('2⬛')
st3 = KeyboardButton('3🟥')

st4 = KeyboardButton('4⬛')
st5 = KeyboardButton('5🟥')
st6 = KeyboardButton('6⬛')

st7 = KeyboardButton('7🟥')
st8 = KeyboardButton('8⬛')
st9 = KeyboardButton('9🟥')

st10 = KeyboardButton('10⬛')
            #10
st11 = KeyboardButton('11⬛')
st12 = KeyboardButton('12🟥')

st13 = KeyboardButton('13⬛')
st14 = KeyboardButton('14🟥')
st15 = KeyboardButton('15⬛')

st16 = KeyboardButton('16🟥')
st17 = KeyboardButton('17⬛')
st18 = KeyboardButton('18🟥')

st19 = KeyboardButton('19🟥')
st20 = KeyboardButton('20⬛')
st21 = KeyboardButton('21🟥')
            #20
st22 = KeyboardButton('22⬛')
st23 = KeyboardButton('23🟥')
st24 = KeyboardButton('24⬛')

st25 = KeyboardButton('25🟥')
st26 = KeyboardButton('26⬛')
st27 = KeyboardButton('27🟥')

st28 = KeyboardButton('28⬛')
st29 = KeyboardButton('29⬛')
st30 = KeyboardButton('30🟥')

st31 = KeyboardButton('31⬛')
st32 = KeyboardButton('32🟥')
            #30
st33 = KeyboardButton('33⬛')

st34 = KeyboardButton('34🟥')
st35 = KeyboardButton('35⬛')
st36 = KeyboardButton('36🟥')
st1to18 = KeyboardButton('1 to 18')
st19to36 = KeyboardButton('19 to 36')
st112 = KeyboardButton('1st 12')
st212 = KeyboardButton('2nd 12')
st312 = KeyboardButton('3rd 12')
stred = KeyboardButton('Red🟥')
stblack = KeyboardButton('Black⬛')

rul = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi).add(st0).row(st1,st2,st3).row(st4,st5,st6).row(st7,st8,st9).row(st10,st11,st12).row(st13,st14,st15).row(st16,st17,st18).row(st19,st20,st21).row(st22,st23,st24).row(st25,st6,st27).row(st28,st29,st30).row(st31,st32,st33).row(st34,st35,st36).row(st1to18,st19to36).row(st112,st212,st312).row(stred,stblack)
button_hi = KeyboardButton('🙍‍♂️Личный кабинет🙍‍♂️')
button_hi2 = KeyboardButton('💵Пополнить💵')
button_hi3 = KeyboardButton('💸Вывод💸')
button_hi4 = KeyboardButton('📈Краш📈')
button_hi5 = KeyboardButton('🎰Рулетка🎰')
button_hi6 = KeyboardButton('🎲Кости🎲')
pom = KeyboardButton('ЧаВо?📑')
qiwi = KeyboardButton('Киви🥝')
card = KeyboardButton('Карта💳')
bon = KeyboardButton('Бонус🎁')
keyb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi).row(button_hi2,button_hi3).row(button_hi4,button_hi5,button_hi6).add(pom).add(qiwi, card).add(bon)

