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
    
class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField(max_length=50)
    medal = models.CharField(max_length=10, blank=True, choices=MedalType)

    def __str__(self):
        return self.name + " - " + self.medal
    
### Realtionships-------------------------------------------------------------------------------------------------------

## Many-to-One
# a Manufacturer makes multiple cars but each Car only has one Manufacturer

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # company_that_makes_it = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

# c.manufacturer
# m.car_set

## Many-to-Many
# a Topping can be on multiple pizzas and each Pizza has multiple toppings

class Topping(models.Model):
    name = models.CharField(max_length=50)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)


class Personn(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=50)
    # we use through argument to point to the model that will act as an intermediary
    members = models.ManyToManyField(Personn, through="Memebership")

class Membership(models.Model):
    personn = models.ForeignKey(Personn, on_delete=models.CASCADE)
    group   = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    invite_reason = models.CharField(max_length=50)