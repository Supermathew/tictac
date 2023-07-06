from django.db import models

# Create your models here.


class Game(models.Model):
    room_code = models.CharField(max_length=100)
    game_creator = models.CharField(max_length=100)
    game_opponent = models.CharField(max_length=100 , blank=True , null=True)
    is_over = models.BooleanField(default=False)
    one = models.CharField(max_length=225,default="start")
    two = models.CharField(max_length=225,default="start")
    three = models.CharField(max_length=225,default="start")
    four = models.CharField(max_length=225,default="start")
    five = models.CharField(max_length=225,default="start")
    six = models.CharField(max_length=225,default="start")
    seven = models.CharField(max_length=225,default="start")
    eight = models.CharField(max_length=225,default="start")
    nine = models.CharField(max_length=225,default="start")

