from django.contrib import admin
from animals.models import (
    Animal,
    Class,
    Family,
    Specie,
)

admin.site.register(Animal)
admin.site.register(Class)
admin.site.register(Family)
admin.site.register(Specie)
