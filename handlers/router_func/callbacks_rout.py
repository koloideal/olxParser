from aiogram import types
from get_data.olx_parser import parser


async def callbacks_rout(callback: types.CallbackQuery) -> None:

    full_url = 'https://www.olx.kz/' + callback.data

    process = await callback.message.answer('Parsing in progress...')

    result_data = await parser(full_url)

    await process.delete()

    for data in result_data:

        await callback.message.answer(f'🗂 Название: {data['title']}\n'
                                      f'💰 Цена: {data['price']}\n'
                                      f'📍 Местоположение: {data['locate']}\n'
                                      f'🗒 Описание: {data['description']}\n\n'
                                      f'👤 Продавец: {data['author_name']}\n'
                                      f'📅 Дата публикации: {data['date']}\n'
                                      f'📅 Дата регистрации: {data['on_olx']}\n\n'
                                      f'📞 Номер: {data['phone']}\n\n'
                                      f'🔗 <a href="{data['link']}">Ссылка на объявление</a>\n'
                                      f'🔗 <a href="{data['link_img']}">Ссылка на фото</a>',
                                      parse_mode='HTML', disable_web_page_preview=True)
