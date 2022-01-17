from django.db import models
from shared.django.model import DeleteModel


class Burger(DeleteModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=70)
    image = models.ImageField(upload_to='burgers/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
