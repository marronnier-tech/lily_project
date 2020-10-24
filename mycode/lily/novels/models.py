from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


class Story(models.Model):

    title = models.CharField(max_length=100)
    URL = models.CharField("URL", max_length=50)
    author = models.CharField("author", max_length=20)
    abstract = models.TextField("abstract", max_length=1000, blank=True)
    favorite = models.PositiveIntegerField("favorite", default=0)
    year = models.IntegerField("year",
                               validators=[MinValueValidator(2000), MaxValueValidator(2030)])
    month = models.IntegerField("month",
                                validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField("day",
                              validators=[MinValueValidator(1), MaxValueValidator(31)], )
    hour = models.IntegerField("hour",
                               validators=[MinValueValidator(0), MaxValueValidator(23)])
    minute = models.IntegerField("minute",
                                 validators=[MinValueValidator(0), MaxValueValidator(59)])

    def __str__(self):
        return self.title


"""

class Novel(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



"""
