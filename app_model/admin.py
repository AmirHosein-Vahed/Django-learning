from django.contrib import admin
from .models import Person, Musician, Album, Student, Runner, \
Manufacturer, Car, Topping, Pizza

# Register your models here.
admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Student)
admin.site.register(Runner)

admin.site.register(Manufacturer)
admin.site.register(Car)

admin.site.register(Topping)
admin.site.register(Pizza)