from django.db import models

# Create your models here.
class Person(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
        }
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default="M")

    def __str__(self):
        return self.first_name + " " + self.last_name

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_starts = models.IntegerField()

    def __str__(self):
        return self.name + " - " + str(self.artist)

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ("FR", "Freshman"),
        ("SO", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
        ("GR", "Graduate"),
        ]
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)

    def __str__(self):
        return self.name + " - " + self.year