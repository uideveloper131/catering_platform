from django.db import models
from brands.models import Brand


class Category(models.Model):

    name=models.CharField(
        max_length=100
    )

    active=models.BooleanField(
        default=True
    )


    def __str__(self):

        return self.name



class MenuItem(models.Model):

    brand=models.ForeignKey(

        Brand,

        on_delete=models.CASCADE
    )

    category=models.ForeignKey(

        Category,

        on_delete=models.CASCADE
    )

    name=models.CharField(

        max_length=100
    )

    image=models.ImageField(

        upload_to='menu/',
        blank=True,
        null=True
    )

    available=models.BooleanField(

        default=True
    )


    def __str__(self):

        return self.name