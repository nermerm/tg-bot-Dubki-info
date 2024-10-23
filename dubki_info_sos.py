import random
import asyncio
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile

bot = Bot(token='7514549733:AAHX8Je_JdOQCZvttkNs5k3MiBoH9y-0glE')
dp = Dispatcher()
router = Router()

#ГЛАВНОЕ МЕНЮ
@router.message(Command('start'))
@router.message(F.text.lower() == "в начало")
async def send_welcome(message: Message):
    kb = [
        [
            types.KeyboardButton(text="Дубовозка"),
            types.KeyboardButton(text="Погода"),
            types.KeyboardButton(text="Контакты Студсовета"),
            types.KeyboardButton(text="Кастелянная"),
            types.KeyboardButton(text="Анекдот")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Привет! Я бот-помощник студентам Вышки, проживающим в Дубках. Как я могу тебе помочь?", reply_markup=keyboard)

#СТУДСОВЕТ - выдает контакты студсовета Дубков сообщением
@router.message(F.text.lower() == "контакты студсовета" )
async def studsovet(message:Message):
    print(message)
    await message.answer(f'Контакты студсовета: \n'
                         f'@rafa_peach - Равшан - председатель Студсовета \n'
                         f'@ProgreSSSR - Алексей - обудсмен \n'
                         f'@khanapiyayev - Бунёд - по делам дубовозок \n')

#РАБОТА КАСТЕЛЯННОЙ - отправляет фото расписания кастелянной каждого корпуса
@router.message(F.text.lower() == "кастелянная")
async def all_kastel(message:Message):
    kb = [
        [
            types.KeyboardButton(text="1 корпус"),
            types.KeyboardButton(text="2 корпус"),
            types.KeyboardButton(text="3 корпус")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Выбери корпус!", reply_markup=keyboard)

@router.message(F.text == "1 корпус") #отправит фото расписания кастелянной 1-го корпуса
async def kastel_1k(message:Message):
    kast_1 = FSInputFile("kastelyannaya1k.jpg")
    kb = [
        [
            types.KeyboardButton(text="2 корпус"),
            types.KeyboardButton(text="3 корпус"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer_photo(kast_1, caption="График работы кастелянной в 1ом корпусе")
    await message.answer("Вернуться в начало?", reply_markup=keyboard)

@router.message(F.text == "2 корпус") #отправит фото расписания кастелянной 2-го корпуса
async def kastel_1k(message:Message):
    kast_1 = FSInputFile("kastelyannaya2k.jpg")
    kb = [
        [
            types.KeyboardButton(text="1 корпус"),
            types.KeyboardButton(text="3 корпус"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer_photo(kast_1, caption="График работы кастелянной в 2ом корпусе")
    await message.answer("Вернуться в начало?", reply_markup=keyboard)

@router.message(F.text == "3 корпус") #отправит фото расписания кастелянной 3-го корпуса
async def kastel_1k(message:Message):
    kast_1 = FSInputFile("kastelyannaya3k.jpg")
    kb = [
        [
            types.KeyboardButton(text="1 корпус"),
            types.KeyboardButton(text="2 корпус"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer_photo(kast_1, caption="График работы кастелянной в 3ем корпусе")
    await message.answer("Вернуться в начало?", reply_markup=keyboard)

#ПОГОДА - показывает погоду в Дубках и в Москве по инлайн-кнопке
@router.message(F.text.lower() == "погода")
async def all_weather(message:Message):
    kb = [
        [
            types.KeyboardButton(text="В Дубках"),
            types.KeyboardButton(text="В Москве")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Где?", reply_markup=keyboard)

@router.message(F.text.lower() == "в дубках")
@router.message(F.text.lower() == "погода в дубках") #выдает инлайн-кнопку с ссылкой на погоду в дубках
async def weather_dubki(message:Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Погода в Дубках",
        url="https://www.gismeteo.ru/weather-dubki-168414/"
    ))
    kb = [
        [
            types.KeyboardButton(text="Погода в Москве"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Вот твоя ссылка:", reply_markup=builder.as_markup())
    await message.answer("Вернуться в начало?", reply_markup=keyboard)

@router.message(F.text.lower() == "в москве")
@router.message(F.text.lower() == "погода в москве") #выдает инлайн-кнопку с ссылкой на погоду в москве
async def weather_msk(message:Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Погода в Москве",
        url="https://www.gismeteo.ru/weather-moscow-4368/"
    ))
    kb = [
        [
            types.KeyboardButton(text="Погода в Дубках"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Вот твоя ссылка:", reply_markup=builder.as_markup())
    await message.answer("Вернуться в начало?", reply_markup=keyboard)

#АНЕКДОТ - выдает рандомный анекдот из файла для поднятия настроение :)
@router.message(F.text.lower() == "анекдот")
async def anecdot(message:Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Хочу анекдот!",
        callback_data='anec'
    ))
    await message.answer("Я могу рассказать тебе анекдот:)", reply_markup=builder.as_markup())

@dp.callback_query(F.data == 'anec')
async def rand_anecdot(callback:types.CallbackQuery):
    file = open('anecdots.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    index = random.randint(0, len(lines) - 1)
    random_line = lines[index]
    file.close()
    await callback.message.answer(random_line)
    await callback.answer()

#ДУБОВОЗКИ - в них много всяких фич
@router.message(F.text.lower() == "дубовозка")
async def all_about_dubovozki(message:Message):
    kb = [
        [
            types.KeyboardButton(text="Ближайшие автобусы"),
            types.KeyboardButton(text="Расписание"),
            types.KeyboardButton(text="Где остановки?"),
            types.KeyboardButton(text="Тгк с инфой"),
            types.KeyboardButton(text="Контакты")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Как я могу помочь тебе с дубовозками?", reply_markup=keyboard)

@router.message(F.text.lower() == "ближайшие автобусы") #будем выводить по три ближайших автобуса в дубки/из дубков в зависимости от времени отправки сообщения
async def closest_buses(message:Message):
    kb = [
        [
            types.KeyboardButton(text="В Дубки"),
            types.KeyboardButton(text="Из Дубков")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Куда?", reply_markup=keyboard)

@router.message(F.text.lower() == "из дубков") #выводит сообщением по три ближайших автобуса от трех остановок
async def buses(message:Message):
    f = open('dubovozki.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    time = message.date.strftime("%H:%M")
    dep_time = int(time[0:2]) + 3 + 0.01 * int(time[3:5])

    to_odi = list(map(float, lines[0].split()))
    buses_to_odi = []
    for i in range(len(to_odi)):
        if dep_time > to_odi[-1]:
            buses_to_odi = [to_odi[0], to_odi[1], to_odi[2]]
        elif to_odi[i] <= dep_time:
            continue
        else:
            if i + 2 >= len(to_odi):
                buses_to_odi = [to_odi[i], to_odi[i + 1]]
            elif i + 1 >= len(to_odi):
                buses_to_odi = to_odi[i]
            else:
                buses_to_odi = [to_odi[i], to_odi[i + 1], to_odi[i + 2]]
            break
    buses_to_odi1 = ','.join((f'{el:.{2}f}') for el in buses_to_odi)

    to_mol = list(map(float, lines[1].split()))
    buses_to_mol = []
    for i in range(len(to_mol)):
        if dep_time > to_mol[-1]:
            buses_to_mol = [to_mol[0], to_mol[1], to_mol[2]]
        if to_mol[i] <= dep_time:
            continue
        else:
            if i + 2 >= len(to_mol):
                buses_to_mol = [to_mol[i], to_mol[i + 1]]
            elif i + 1 >= len(to_mol):
                buses_to_mol = to_mol[i]
            else:
                buses_to_mol = [to_mol[i], to_mol[i + 1], to_mol[i + 2]]
            break
    buses_to_mol1 = ','.join((f'{el:.{2}f}') for el in buses_to_mol)

    to_slavbul = list(map(float, lines[2].split()))
    buses_to_slavbul = []
    for i in range(len(to_slavbul)):
        if dep_time > to_slavbul[-1]:
            buses_to_slavbul = [to_slavbul[0], to_slavbul[1], to_slavbul[2]]
        elif to_slavbul[i] <= dep_time:
            continue
        else:
            if i + 2 >= len(to_slavbul):
                buses_to_slavbul = [to_slavbul[i], to_slavbul[i + 1]]
            elif i + 1 >= len(to_slavbul):
                buses_to_slavbul = to_slavbul[i]
            else:
                buses_to_slavbul = [to_slavbul[i], to_slavbul[i + 1], to_slavbul[i + 2]]
            break
    buses_to_slavbul1 = ','.join((f'{el:.{2}f}') for el in buses_to_slavbul)
    kb = [
        [
            types.KeyboardButton(text="В Дубки"),
            types.KeyboardButton(text="Из Дубков"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer(f'Ближайшие автобусы до Одинцово:\n{buses_to_odi1}\nБлижайшие автобусы до Молодежной:\n{buses_to_mol1}\nБлижайшие автобусы до Славянского бульвара:\n{buses_to_slavbul1}')
    await message.answer("Вернуться в начало?", reply_markup=keyboard)


@router.message(F.text.lower() == "в дубки") #выводит сообщением по три ближайших автобуса от трех остановок
async def buses(message:Message):
    f = open('dubovozki.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    time = message.date.strftime("%H:%M")
    dep_time = int(time[0:2]) + 3 + 0.01 * int(time[3:5])

    from_odi = list(map(float, lines[3].split()))
    buses_from_odi = []
    if dep_time > from_odi[-1]:
        buses_from_odi = [from_odi[0], from_odi[1], from_odi[2]]
    for i in range(len(from_odi)):
        if from_odi[i] <= dep_time:
            continue
        else:
            if i + 2 >= len(from_odi):
                buses_from_odi = [from_odi[i], from_odi[i + 1]]
            elif i + 1 >= len(from_odi):
                buses_from_odi = from_odi[i]
            else:
                buses_from_odi = [from_odi[i], from_odi[i + 1], from_odi[i + 2]]
            break
    buses_from_odi1 = ','.join((f'{el:.{2}f}') for el in buses_from_odi)

    from_mol = list(map(float, lines[4].split()))
    buses_from_mol = []
    if dep_time > from_mol[-1]:
        buses_from_mol = [from_mol[0], from_mol[1], from_mol[2]]
    for i in range(len(from_mol)):
        if from_mol[i] <= dep_time:
            continue
        else:
            if i + 2 >= len(from_mol):
                buses_from_mol = [from_mol[i], from_mol[i + 1]]
            elif i + 1 >= len(from_mol):
                buses_from_mol = from_mol[i]
            else:
                buses_from_mol = [from_mol[i], from_mol[i + 1], from_mol[i + 2]]
            break
    buses_from_mol1 = ','.join((f'{el:.{2}f}') for el in buses_from_mol)

    from_slavbul = list(map(float, lines[5].split()))
    buses_from_slavbul = []
    if dep_time > from_slavbul[-1]:
        buses_from_slavbul = [from_slavbul[0], from_slavbul[1], from_slavbul[2]]
    for i in range(len(from_slavbul)):
        if from_slavbul[i] <= dep_time:
            continue
        else:
            if i + 2 >= len(from_slavbul):
                buses_from_slavbul = [from_slavbul[i], from_slavbul[i + 1]]
            elif i + 1 >= len(from_slavbul):
                buses_from_slavbul = from_slavbul[i]
            else:
                buses_from_slavbul = [from_slavbul[i], from_slavbul[i + 1], from_slavbul[i + 2]]
            break
    buses_from_slavbul1 = ','.join((f'{el:.{2}f}') for el in buses_from_slavbul)
    kb = [
        [
            types.KeyboardButton(text="Из Дубков"),
            types.KeyboardButton(text="В Дубки"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer(f'Ближайшие автобусы от Одинцово:\n{buses_from_odi1}\nБлижайшие автобусы от Молодежной:\n{buses_from_mol1}\nБлижайшие автобусы от Славянского бульвара:\n{buses_from_slavbul1}')
    await message.answer("Вернуться в начало?", reply_markup=keyboard)

@router.message(F.text.lower() == "расписание") #отправит фото расписания автобусов по будням
async def buses(message: Message):
    rasp_dubovozki = FSInputFile("rasp.jpg")
    kb = [
        [
            types.KeyboardButton(text="Дубовозка"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer_photo(rasp_dubovozki, caption="Расписание дубовозок по будням")
    await message.answer("Вернуться в начало?", reply_markup=keyboard)

@router.message(F.text.lower() == "где остановки?") #отправит инлайн-кнопки с ссылками на локации остановок
async def stations(message:Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="На Одинцово",
        url="https://yandex.ru/maps/117555/vniissok/stops/stop__10100145/?indoorLevel=1&ll=37.226461%2C55.661369&tab=overview&z=17.06",
    ))
    builder.add(types.InlineKeyboardButton(
        text="На Славянский бульвар",
        url="https://yandex.ru/maps/117555/vniissok/stops/stop__10100145/?indoorLevel=1&ll=37.226461%2C55.661369&tab=overview&z=17.06",
    ))
    builder.add(types.InlineKeyboardButton(
        text="На Молодежную",
        url="https://yandex.ru/maps/1/moscow-and-moscow-oblast/stops/stop__10206524/?indoorLevel=1&ll=37.226461%2C55.661369&tab=overview&z=17.06",
    ))
    builder.add(types.InlineKeyboardButton(
        text="Из Одинцово",
        url="https://yandex.ru/maps/10743/odincovo/stops/4082525635/?ll=37.279179%2C55.671855&tab=overview&z=18.22",
    ))
    builder.add(types.InlineKeyboardButton(
        text="От Молодежной",
        url="https://yandex.ru/maps/213/moscow/stops/stop__9724412/?indoorLevel=1&ll=37.415864%2C55.740082&tab=overview&z=17.95",
    ))
    builder.add(types.InlineKeyboardButton(
        text="От Славянского бульвара",
        url="https://yandex.ru/maps/213/moscow/stops/2081245620/?ll=37.473338%2C55.728856&tab=overview&z=19.08",
    ))
    kb = [
        [
            types.KeyboardButton(text="Дубовозка"),
            types.KeyboardButton(text="В начало")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Вот все остановки:", reply_markup=builder.as_markup())
    await message.answer("Вернуться в начало?", reply_markup=keyboard)

@router.message(F.text.lower() == "тгк с инфой") #отправит ник телеграмм-канала "Движение Бубков"
async def tgchannel(message:Message):
    await message.answer("@dubovozki - канал со всей информацией о дубовозках")

@router.message(F.text.lower() == "контакты") #отправит контакты ответсвенных за автобусы
async def contacts(message:Message):
    await message.answer("+79853320438 - контакт менеджера\n"
                         "@khanapiyayev - Бунёд - студсоветчик, ответственный за дубовозки\n"
                         "@rafa_peach - Равшан - председатель студсовета")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
