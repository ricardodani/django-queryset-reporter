from django.db import models
from django.contrib.auth.models import User

_CHAR = dict(max_length=255)
_FKEY = dict(on_delete=models.CASCADE)


class _BaseModel(models.Model):
    name = models.CharField(**_CHAR)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return self.name if self.name else ''
    class Meta:
        abstract = True


class Class(_BaseModel):
    '''Class like Mammalia'''

    phylum = models.CharField(**_CHAR)


class Family(_BaseModel):
    '''Family like Canidae'''

    family_class = models.ForeignKey(Class, **_FKEY)
    order_name = models.CharField(**_CHAR)


class Specie(_BaseModel):
    '''Specie like dog, cat.'''

    family = models.ForeignKey(Family, **_FKEY)
    genus_name = models.CharField(**_CHAR)
    scientific_name = models.CharField(**_CHAR)


class Animal(_BaseModel):
    '''Animal class represents the animal itself.'''

    SEX_CHOICES = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('h', 'Hermaphrodite'),
    )
    specie = models.ForeignKey(Specie, **_FKEY)
    race = models.CharField(blank=True, **_CHAR)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, blank=True)
    photo = models.ImageField(
        height_field='photo_height', width_field='photo_width',
        upload_to='animals', blank=True
    )
    photo_height = models.IntegerField(null=True, blank=True, editable=False)
    photo_width = models.IntegerField(null=True, blank=True, editable=False)
    owners = models.ManyToManyField(User, blank=True)
