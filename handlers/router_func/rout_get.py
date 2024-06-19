from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from database_func.get_banned_users import get_banned_users
from handlers.router_func.rout_start import creator_id


class AdminState(StatesGroup):
    waiting_for_add_admin: State = State()
    waiting_for_del_admin: State = State()
    waiting_for_ban_user: State = State()
    waiting_for_unban_user: State = State()


async def button_to_get_rout(message: Message) -> None:
    user_id: int = message.from_user.id

    banned_users: list = await get_banned_users()

    if (user_id in banned_users) and (user_id != creator_id):

        await message.answer(f"You can't use the bot."
                             f"\n\n<u><b>You were blocked</b></u>"
                             f"\n\n\nAbout the unban - <a href='https://t.me/kolo_id'>kolo</a>",
                             disable_web_page_preview=True)

    else:

        one: InlineKeyboardButton = InlineKeyboardButton(text='Услуги',
                                                         callback_data='uslugi/')

        two: InlineKeyboardButton = InlineKeyboardButton(text='Строительство',
                                                         callback_data='stroitelstvo-remont/')

        three: InlineKeyboardButton = InlineKeyboardButton(text='Аренда товаров',
                                                           callback_data='prokat-tovarov/')

        four: InlineKeyboardButton = InlineKeyboardButton(text='Недвижимость',
                                                          callback_data='nedvizhimost/')

        five: InlineKeyboardButton = InlineKeyboardButton(text='Электроника',
                                                          callback_data='elektronika/')

        six: InlineKeyboardButton = InlineKeyboardButton(text='Дом и сад',
                                                         callback_data='dom-i-sad/')

        seven: InlineKeyboardButton = InlineKeyboardButton(text='Работа',
                                                           callback_data='katehoriya-rabota/')

        eight: InlineKeyboardButton = InlineKeyboardButton(text='Мода и стиль',
                                                           callback_data='moda-i-stil/')

        nine: InlineKeyboardButton = InlineKeyboardButton(text='Хобби и спорт',
                                                          callback_data='hobbi-otdyh-i-sport/')

        ten: InlineKeyboardButton = InlineKeyboardButton(text='Транспорт',
                                                         callback_data='transport/')

        eleven: InlineKeyboardButton = InlineKeyboardButton(text='Животные',
                                                            callback_data='zhivotnye/')

        twelve: InlineKeyboardButton = InlineKeyboardButton(text='Отдам даром',
                                                            callback_data='otdam-darom/')

        thirteen: InlineKeyboardButton = InlineKeyboardButton(text='Детский мир',
                                                              callback_data='detskiy-mir/')

        buttons: list = [

            [one, two, three],
            [four, five, six],
            [seven, eight, nine],
            [ten, eleven, twelve],
            [thirteen]

        ]

        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

        await message.answer('<b>Select needed category for parsing🔎</b>', reply_markup=keyboard)

    return
