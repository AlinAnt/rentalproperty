from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class Communication(models.Model):
    name = models.CharField(max_length=200, help_text="Какие коммуникации присутствуют в данном помещении")

    def __str__(self):
        return self.name


class Area(models.Model):
    square = models.IntegerField(help_text="Площадь помещения")
    typeArea = models.ForeignKey('TypeArea', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(help_text="Цена")
    year = models.DateField(null=True, blank=True)
    floor = models.IntegerField(help_text="На каком этаже находится помещение")
    # надо такой тип, чтобы галочками можно было отметить нужные коммуникации
    communication = models.ManyToManyField(Communication, help_text='Вода, отопление,электрическтво')
    address = models.TextField(help_text="Где находится")
    endOfRental = models.DateField(null=True, blank=True)
    rent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overend(self):
        if self.endOfRental and date.today() > self.endOfRental:
            return True
        return False

    @property
    def is_free(self):
        if self.status == "Free":
            return True
        return False

    RENT_STATUS = (
        ('Free', 'Free'),
        ('Busy', 'Busy'),
    )

    status = models.CharField(
        max_length=4,
        choices=RENT_STATUS,
        blank=True,
        default="Free",
        help_text='Area availability')

    class Meta:
        ordering = ['endOfRental']
        permissions = (("can_mark_singled_out ", "Set area as free"),)

    def __str__(self):
        return '{0} ({1})'.format(self.typeArea, self.square)

    def get_absolute_url(self):
        return reverse('area-detail', args=[str(self.id)])

    def display_communication(self):
        return ','.join([communication.name for communication in self.communication.all()[:3]])
    display_communication.short_description = 'Communication'


class TypeArea(models.Model):
    TYPE_STATUS = (
        ('Office', 'Office'),
        ('Stock', 'Stock'),
        ('Shopping', 'Shopping_center'),

    )
    name = models.CharField(max_length=10, choices=TYPE_STATUS, blank=True, default="Office")

    def get_absolute_url(self):
        return reverse('typearea-detail', args=[str(self.id)])

    def __str__(self):
        return self.name





