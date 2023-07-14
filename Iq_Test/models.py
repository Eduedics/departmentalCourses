from django.db import models
from django.contrib.auth.models import User

class IQQuestion(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class UserIQResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(IQQuestion, on_delete=models.CASCADE)
    response = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.question}"
class UserScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Score: {self.score}"
