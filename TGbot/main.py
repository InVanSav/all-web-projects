import time
import requests
import config
import telebot
import emoji
import os
import zipfile

from moviepy.editor import VideoFileClip
from PIL import Image

bot = telebot.TeleBot(config.TOKEN)
capitan = 889602949


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}!</u></b>' \
           f'{emoji.emojize(":smirk:", language="alias")}' \
           f'\nЯ могу помочь тебе сделать GIF изображение и' \
           f'\nсоздать cвои собственные стикер-паки!{emoji.emojize(":milky_way::fire:", language="alias")}' \
           f'\n\n{message.from_user.first_name}, ты можешь управлять мной' \
           f'\nс помощью этих команд: ' \
           f'\n\n<b>Работа со стикерами:</b>' \
           f'\n/newstickpack - конвертировать JPG/PNG в WEBP' \
           f'\n/correct - редактировать свои паки' \
           f'\n/mystickers - посмотреть свои паки' \
           f'\n\n<b>Работа с видео:</b>' \
           f'\n/convertgif - конвертировать видео в GIF' \
           f'\n/editgifstore - редактировать хранилище GIF' \
           f'\n/mygif - взглянуть на свои GIF' \
           f'\n\n<b>Помощь:</b>' \
           f'\n/whatisit - отправить сообщение разработчику о неисправности' \
           f'\n/verynice - отправить сообщение разработчику о крутости бота' \
           f'\n/description - возможность описать проблему/похвальбу разработчику' \
           f'\n/help - вывести список возможностей бота' \
           f'\n\n```<b><u>ВАЖНО!</u></b>```' \
           f'\nКоманды /whatisit и /verynice работают автоматически. ' \
           f'То есть, вам НЕ нужно самостоятельно что-то писать.'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['newstickpack'])
def create_new_sticker_pack(message):
    mess = f'Чтобы конвертировать JPG/PNG в WEBP, вам необходимо ' \
           f'отправить мне  файл с фотографиями формата JPG/PNG и подождать некоторое время.' \
           f'\nДалее вам придет инструкция.' \
           f'\n\n```<b><u>ОЧЕНЬ ВАЖНО!</u></b>```' \
           f'\n\n- Отправляемый вами файл должен быть назван "Done"' \
           f'\n- Расширение файла .ZIP' \
           f'\n- Фотографии внутри файла должны быть названо ТОЛЬКО по-английски'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['document'])
def get_document(message):
    bot.send_message(message.chat.id, 'Отлично! Теперь подождите, пока ваш файл конвертируется.')

    doc_info = bot.get_file(message.document.file_id)
    doc = requests.get(f'https://api.telegram.org/file/bot{config.TOKEN}/{doc_info.file_path}')

    f = open(r"/Users/vanish/PycharmProjects/telebot/stickers/stick_pack.zip", "wb")
    f.write(doc.content)

    archive = 'stickers/stick_pack.zip'

    with zipfile.ZipFile(archive, 'r') as zip_file:
        zip_file.extractall(".")

    time.sleep(10)
    files = os.listdir(path="./Done")
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    for image in images:
        if image.endswith('jpg'):
            convert_image(image, image_type='jpg')
        elif image.endswith('png'):
            convert_image(image, image_type='png')

    convert_to_zip()
    doc = open("Done.zip", "rb")
    bot.send_document(message.chat.id, doc)

    mess = f'Все успешно завершено!' \
           f'\nДалее вам нужно отправиться к нему @Stickers, ' \
           f'чтобы передать заветный документ, который поможет ' \
           f'успешно завершить создание вашего собственного <b><u>пакета стикеров</u></b>.' \
           f'\n\nРад, что вы доверились мне! (Хотя, разве может быть иначе?)' \
           f'{emoji.emojize(":smirk::fire:", language="alias")}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    os.remove("./Done.zip")


def convert_image(image_path, image_type):
    im = Image.open("./Done/" + image_path)
    im = im.convert('RGB')
    image_name = image_path.split('.')[0]

    if image_type == 'jpg' or image_type == 'png':
        im.save(f"./Done/{image_name}.webp", 'webp')


def convert_to_zip():
    fantasy_zip = zipfile.ZipFile('Done.zip', 'w')

    for folder, subfolders, files in os.walk('./Done/'):
        for file in files:
            if file.endswith('.webp'):
                fantasy_zip.write(os.path.join(folder, file),
                                  os.path.relpath(os.path.join(folder, file), './Done'),
                                  compress_type=zipfile.ZIP_DEFLATED)


@bot.message_handler(commands=['correct'])
def edit_my_stickers(message):
    mess = f'Для твоих файлов база данных нужна.' \
           f'\nТы ведь ее не подключал?' \
           f' Вот и я тоже:)'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['mystickers'])
def check_my_stickers(message):
    mess = f'Для твоих файлов база данных нужна.' \
           f'\nТы ведь ее не подключал?' \
           f' Вот и я тоже:)'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['convertgif'])
def message_conveter_gif_file(message):
    mess = f'Чтобы конвертировать видео в GIF, вам необходимо ' \
           f'отправить мне просто видео (не видео файл) длиной 2-3 секунды и подождать некоторое время.'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['video'])
def converter_gif_file(message):
    bot.send_message(message.chat.id, 'Отлично! Теперь подождите, пока ваше видео конвертируется.')

    video_info = bot.get_file(message.video.file_id)
    video = requests.get(f'https://api.telegram.org/file/bot{config.TOKEN}/{video_info.file_path}')

    f = open(r"/Users/vanish/PycharmProjects/telebot/videos/video.mp4", "wb")
    f.write(video.content)

    video_clip = VideoFileClip("videos/video.mp4")
    video_clip.write_gif(f"videos/{message.from_user.username}.gif")

    gif = open(f"videos/{message.from_user.username}.gif", "rb")
    bot.send_document(message.chat.id, gif)
    bot.send_message(message.chat.id, f'{emoji.emojize("Готово!:milky_way::fire:", language="alias")}')

    os.remove(f"videos/{message.from_user.username}.gif")
    os.remove("videos/video.mp4")


@bot.message_handler(commands=['editgifstore'])
def edit_gif_storage(message):
    mess = f'Для твоих файлов база данных нужна.' \
           f'\nТы ведь ее не подключал?' \
           f' Вот и я тоже:)'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['mygif'])
def check_my_gifs(message):
    mess = f'Для твоих файлов база данных нужна.' \
           f'\nТы ведь ее не подключал?' \
           f' Вот и я тоже:)'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['whatisit'])
def what_is_it(message):
    user_mess = f'<b>Я кожанному передал твой username: <u>@{message.from_user.username}</u>!</b>' \
                f'\nДальше как-то сам выкручивайся' \
                f'{emoji.emojize(":eyes:", language="alias")}'
    mess = f'Кэп, у нас проблемы! Где-то баг.' \
           f'{emoji.emojize(":shit:", language="alias")}' \
           f'\nВот у него что-то произошло:' \
           f'\n\nid:{message.from_user.id}' \
           f'\n@{message.from_user.username}'
    bot.send_message(capitan, mess, parse_mode='html')
    bot.send_message(message.chat.id, user_mess, parse_mode='html')


@bot.message_handler(commands=['verynice'])
def very_nice(message):
    user_mess = f'<b>Ваша похвальба отправлена кожанному!</b>' \
                f'\nДелайте так почаще, а то ему там скучно{emoji.emojize(":grin:", language="alias")}'
    mess = f'Кэп, нас похвалили!' \
           f'{emoji.emojize(":smirk::fire:", language="alias")}' \
           f'\nОн сказал, что мы красавчики:' \
           f'\n\nid:{message.from_user.id}' \
           f'\n@{message.from_user.username}'
    bot.send_message(capitan, mess, parse_mode='html')
    bot.send_message(message.chat.id, user_mess, parse_mode='html')


@bot.message_handler(commands=['description'])
def description(message):
    mess = f'Введите ваше сообщение и отправьте боту.' \
           f'\nОно будет автоматически отправлено разработчику.'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def feed_back(message):
    if message.text == '/help':
        help_func(message)
    else:
        mess_user = f'{message.from_user.first_name},' \
                    f' ваше сообщение было успешно отправлено!' \
                    f'{emoji.emojize(":eyes:", language="alias")}'

        mess_capitan = f'{message.text}' \
                       f'\n\nid:{message.from_user.id}' \
                       f'\n@{message.from_user.username}'

        bot.send_message(message.chat.id, mess_user, parse_mode='html')
        bot.send_message(capitan, mess_capitan, parse_mode='html')


def help_func(message):
    mess = f'\n\n{message.from_user.first_name}, ты можешь управлять мной' \
           f'\nс помощью этих команд: ' \
           f'\n\n<b>Работа со стикерами:</b>' \
           f'\n/newstickpack - создать новый пак стикеров' \
           f'\n/correct - редактировать свои паки' \
           f'\n/mystickers - посмотреть свои паки' \
           f'\n\n<b>Работа с видео:</b>' \
           f'\n/convertgif - конвертировать видео в GIF' \
           f'\n/editgifstore - редактировать хранилище GIF' \
           f'\n/mygif - взглянуть на свои GIF' \
           f'\n\n<b>Помощь:</b>' \
           f'\n/whatisit - отправить сообщение разработчику о неисправности' \
           f'\n/verynice - отправить сообщение разработчику о крутости бота' \
           f'\n/description - возможность описать проблему/похвальбу разработчику' \
           f'\n\n```<b><u>ВАЖНО!</u></b>```' \
           f'\nКоманды /whatisit и /verynice работают автоматически. ' \
           f'То есть, вам НЕ нужно самостоятельно что-то писать.'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)
