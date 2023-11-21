import json
from telegram import Update
from telegram.ext import Updater, CallbackContext, TypeHandler

def overwriting(update:Update,context: CallbackContext):
    domen = "https://www."
    if domen in update.message.text:
        text = update.message.text.replace("www.","dd")
        update.message.reply_text(text)
        context.bot.delete_message(update.message.chat_id,update.message._id_attrs[0])
    else:
        update.message.reply_text("Это не сылка")
        context.bot.delete_message(update.message.chat_id, update.message._id_attrs[0])


def main():
    updater = Updater("6604273995:AAFUyB7klkCWh7MtzhfVOdfZCdnHjpbk7qw")
    updater.dispatcher.add_handler(TypeHandler(Update,overwriting))
    updater.start_polling()

    print('Started')

    updater.idle()


if __name__ == "__main__":
    main()