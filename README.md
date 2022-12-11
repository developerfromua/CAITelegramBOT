Character AI Telegram BOT

Для работы нужен токен бота (получить у BotFather) и токен авторизации.

Чтобы узнать свой токен авторизации заходим в любой диалог, жмём F12 - Networking. Пишем любое сообщение, появляется /streaming, нажимаем, открываем вкладку Headers - Request Headers - authorization. ПКМ - copy value.

Ну и соотвественно вставить свои значени в

bot = telebot.TeleBot('111111111:111111111111111111111111') #Bot Father
token = 'Token 1111111111111111111111111111111111111111' #F12 - Networking 
