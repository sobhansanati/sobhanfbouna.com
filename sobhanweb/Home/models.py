from django.db import models




class Email_sender(models.Model):
    Sender = models.EmailField()
    def __str__(self):
        return self.Sender

class time(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
