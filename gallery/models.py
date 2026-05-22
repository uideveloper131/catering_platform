from django.db import models


class Gallery(models.Model):

    title=models.CharField(
        max_length=100
    )

    image=models.ImageField(
        upload_to='gallery/'
    )

    category=models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    active=models.BooleanField(
        default=True
    )

    created=models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title