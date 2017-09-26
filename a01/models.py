from django.core import serializers
from django.db import models
from django.conf import settings
# from a01.base import baseModel
from django.contrib.postgres.fields import ArrayField
from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxValueValidator, MinValueValidator


class ToJson(object):

    def to_json(self):

        return serializers.serialize('json', self.objects.all())


fs = FileSystemStorage(location=settings.STATIC_ROOT)

# Create your models here.


class Movie(models.Model, ToJson):
    title = models.CharField(max_length=100)
    genre = ArrayField(models.CharField(max_length=50, blank=True))
    runtime = models.PositiveIntegerField()
    category = models.CharField(max_length=10)
    release_date = models.DateField()
    img = models.ImageField(upload_to="wap/templates/static/images/movies/", storage=fs)
    yurl = models.URLField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    director = models.CharField(max_length="50")
    screenplay = models.CharField(max_length="50")
    composer = models.CharField(max_length="50")
    producers = ArrayField(models.CharField(max_length="50"), null=True, blank=True)



    def __str__(self):
        """String representation of model."""
        return self.title


class Hall(models.Model, ToJson):
    number = models.CharField(max_length=5)
    capacity = models.PositiveIntegerField(default=400)

    def __str__(self):
        """String representation of model."""
        return self.number


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
        size=20, blank=True, null=True
    )
    totalcustomer = models.PositiveIntegerField(default=0)

    movie = models.ForeignKey(Movie)
    hall = models.ForeignKey(Hall)

    def __str__(self):
        """String representation of model."""
        return self.movie.title + ' ' + self.hall.number

    @property
    def capacity(self):
        return self.hall.capacity


class Customer(models.Model, ToJson):
    email = models.EmailField()
    screen = models.ForeignKey(Screening)
    seats = models.PositiveIntegerField(validators=[MaxValueValidator(400)])
    bseats = ArrayField(
        ArrayField(
            models.IntegerField(
                default=0,
                validators=[MaxValueValidator(19), MinValueValidator(0)]),
            size=2,
        ),
        size=20, blank=True, null=True
    )

    def __str__(self):
        """String representation of model."""
        return self.email


class Payment(models.Model, ToJson):
    customer = models.ForeignKey(Customer)
    cardnum = models.CharField(max_length=30)
    expdate = models.DateField()
    startdate = models.DateField()

    def __str__(self):
        """String representation of model."""
        return self.customer.email
