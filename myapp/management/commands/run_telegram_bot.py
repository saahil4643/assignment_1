from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler
from myapp.models import TelegramUser

BOT_TOKEN = '7485084503:AAGkPckqx9ML87PnaPP6jsvVAFlBy7dmoKY'

def start(update, context):
    user = update.effective_user
    TelegramUser.objects.get_or_create(
        telegram_id=user.id,
        defaults={
            'username': user.username,
            'first_name': user.first_name,
        }
    )
    update.message.reply_text(f"Hi {user.first_name}, you've been registered!")

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **options):
        updater = Updater(BOT_TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler('start', start))

        self.stdout.write(self.style.SUCCESS('Bot is polling...'))
        updater.start_polling()
        updater.idle()
