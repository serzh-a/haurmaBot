from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Контакты')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')

catalog_list = InlineKeyboardMarkup(row_width=3)
catalog_list.add(InlineKeyboardButton(text='Орехи', callback_data='t-orehi'),
                 InlineKeyboardButton(text='Сухофрукты', callback_data='suhofruct'),
                 InlineKeyboardButton(text='Фрукты', callback_data='fruct'),
                 InlineKeyboardButton(text='Овощи', callback_data='ovohi'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')
