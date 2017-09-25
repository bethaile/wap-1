from django.core import serializers
from django.db import models
# from a01.base import baseModel
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator


class ToJson(object):

    def to_json(self):

        return serializers.serialize('json', self.objects.all())


# Create your models here.


class Movie(models.Model, ToJson):
    title = models.CharField(max_length=100)
    genre = ArrayField(models.CharField(max_length=50, blank=True))
    runtime = models.PositiveIntegerField()
    category = models.CharField(max_length=10)
    release_date = models.DateField()
    img = models.ImageField(upload_to="movies/")
    yurl = models.URLField(max_length=500, null=True, blank=True)


class Hall(models.Model, ToJson):
    number = models.CharField(max_length=5)
    capacity = models.PositiveIntegerField(default=400)


class Screening(models.Model, ToJson):
    stime = models.TimeField()
    sdate = models.DateField()
    seats = ArrayField(
        ArrayField(
            models.IntegerField(
                default=0,
                validators=[MaxValueValidator(1), MinValueValidator(0)]),
            size=20,
        ),
        size=20,
    )

    movie = models.ForeignKey(Movie)
    hall = models.ForeignKey(Hall)

    @property
    def capacity(self):
        return self.hall.capacity


class Customer(models.Model, ToJson):
    email = models.EmailField()
    screen = models.ForeignKey(Screening)
    seats = models.PositiveIntegerField(validators=[MaxValueValidator(400)])


class Payment(models.Model, ToJson):
    cardnum = models.CharField(max_length=30)
    expdate = models.DateField()
    startdate = models.DateField()
