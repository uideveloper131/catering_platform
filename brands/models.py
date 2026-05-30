from django.db import models
from django.urls import reverse


class Brand(models.Model):

    name=models.CharField(
        max_length=100
    )

    description=models.TextField(
        blank=True,
        null=True
    )

    image=models.ImageField(
        upload_to='brands/',
        blank=True,
        null=True
    )

    active=models.BooleanField(
        default=True
    )

    created=models.DateTimeField(
        auto_now_add=True
    )

    def get_absolute_url(self):
        return reverse(
            'brand_detail',
            args=[self.id]
        )

    def __str__(self):
        return self.name