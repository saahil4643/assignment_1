from django.db import models

class Message(models.Model):
    content = models.CharField(max_length=255)
    is_protected = models.BooleanField(default=False)

    def __str__(self):
        return self.content


from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or str(self.telegram_id)
