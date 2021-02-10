from pyrogram import Client, filters  # телеграм клиент

import shelve  # файловая база данных

db = shelve.open('data.db', writeback=True)

# Создать можно на my.telegram.org
API_ID = 2010220
API_HASH = '7328ad673b632c082867bb0fb36333fc'

PRIVATE_PUBLIC = 'hohohohohoohohohohok'  # скрытый паблик для управления ботом zo7g02h
PUBLIC_PUBLIC = 'My_clear_public'  # паблик куда будем репостить
SOURCE_PUBLICS = [
    # список чатов-доноров, откуда бот будет пересылать посты
    'krngldngkjnk',
    'seochat',

]
PHONE_NUMBER = '+79605282601'  # номер зарегистрованный в телеге

# создаем клиент телеграм
app = Client("cyberpunk1", api_id=API_ID, api_hash=API_HASH,
             phone_number=PHONE_NUMBER)


# обработчик нового сообщения
# вызывается при появлении нового поста в одном из пабликов-доноров
@app.on_message(filters.chat(SOURCE_PUBLICS))
def new_channel_post(client, message):
    if moderation_post(client, message):
        forward_message(message, client)


def forward_message(message, client):
    app.forward_messages(PUBLIC_PUBLIC, message.chat.username, message.message_id)
    client.send_message(PUBLIC_PUBLIC, 'Кто: ' + str(app.get_users(message.username)))
    client.send_message(PUBLIC_PUBLIC, 'Из чатика: ' + str(message.chat.username))
    return



# Модерация поста
def moderation_post(client, message):
    try:
        black_list = ['реклама', 'Реклама', 'купить', 'Купить', 'Карам', 'магазин']
        if message.media == True:
            text = message.caption
            print(text)
        else:
            text = message.text

        for word in black_list:
            if word in text:
                print('НАШЛИ!')
                print(message.text)
                return True
        print('Сообщение:')
        print(message.text)
        print('Ничего не нашил и вышли из функции Модерация')
        return False
    except TypeError:
        print('Тип сообщения не текст')
        return False




if __name__ == '__main__':
    print('Atempt to run telegrabber')
    app.run()  # эта строка запустит все обработчики
