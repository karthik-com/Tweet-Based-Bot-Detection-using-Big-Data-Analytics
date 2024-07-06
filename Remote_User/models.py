from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Tweet_Message(models.Model):

    idno= models.CharField(max_length=300)
    Tweet= models.CharField(max_length=300)
    following= models.CharField(max_length=300)
    followers= models.CharField(max_length=300)
    actions= models.CharField(max_length=300)
    is_retweet= models.CharField(max_length=300)
    location= models.CharField(max_length=300)


class Tweet_Type_Prediction(models.Model):

    idno = models.CharField(max_length=300)
    Tweet = models.CharField(max_length=300)
    following = models.CharField(max_length=300)
    followers = models.CharField(max_length=300)
    actions = models.CharField(max_length=300)
    is_retweet = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    tweet_type = models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



