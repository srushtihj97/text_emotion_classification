from django.db import models
from django.utils import timezone


# Create your models here.
class EmotionLog(models.Model):
    input_text = models.TextField(default=None)
    emotion = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'emotion_log'
        verbose_name = 'EmotionLog'

    def __str__(self):
        return f'EmotionLog (input_text={self.input_text}, emotion={self.emotion})'
