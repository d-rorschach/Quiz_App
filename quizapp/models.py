from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class player(models.Model):
    score = models.IntegerField(default=0)
    current_question_no = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Questions(models.Model):
    questions_id = models.AutoField
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)
    image = models.FileField(upload_to="quizapp/image", null=True, blank=True)
    audio = models.FileField(upload_to="quizapp/audio", null=True, blank=True)

