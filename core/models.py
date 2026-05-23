from django.db import models


class FAQ(models.Model):

    question=models.CharField(
        max_length=300
    )
    answer=models.TextField()
    active=models.BooleanField(
        default=True
    )
    created=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.question


class Service(models.Model):

    title=models.CharField(
        max_length=100
    )
    image=models.ImageField(
        upload_to='services/'
    )
    description=models.TextField()
    active=models.BooleanField(
        default=True
    )
    created=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title

class Testimonial(models.Model):

    customer_name=models.CharField(
        max_length=100
    )
    review=models.TextField()
    rating=models.IntegerField(
        default=5
    )
    active=models.BooleanField(
        default=True
    )
    created=models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.customer_name

class ContactInfo(models.Model):

    address=models.TextField()

    phone=models.CharField(
        max_length=20
    )

    email=models.EmailField()

    business_hours=models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    google_map=models.URLField(
        blank=True,
        null=True
    )

    facebook=models.URLField(
        blank=True,
        null=True
    )

    instagram=models.URLField(
        blank=True,
        null=True
    )

    youtube=models.URLField(
        blank=True,
        null=True
    )

    active=models.BooleanField(
        default=True
    )

    def __str__(self):

        return self.email



class ContactMessage(models.Model):

    full_name=models.CharField(
        max_length=100
    )

    email=models.EmailField()

    subject=models.CharField(
        max_length=200
    )

    message=models.TextField()

    created=models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.full_name

class CTASection(models.Model):
    title=models.CharField(
        max_length=200
    )

    description=models.TextField()
    button_text=models.CharField(
        max_length=50,
        default='Request Quote'
    )
    active=models.BooleanField(
        default=True
    )
    created=models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):

        return self.title

class Statistic(models.Model):
    title=models.CharField(
        max_length=100
    )
    value=models.CharField(
        max_length=50
    )
    active=models.BooleanField(
        default=True
    )
    created=models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.title

class OfferPackage(models.Model):

    title=models.CharField(
        max_length=200
    )

    subtitle=models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    image=models.ImageField(
        upload_to='offers/',
        blank=True,
        null=True
    )

    price=models.CharField(
        max_length=50
    )

    description=models.TextField()

    active=models.BooleanField(
        default=True
    )

    created=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title

class PackageFeature(models.Model):
    package=models.ForeignKey(
        OfferPackage,

        on_delete=models.CASCADE,
        related_name='features'
    )
    feature=models.CharField(
        max_length=200
    )


    def __str__(self):
        return self.feature


class EventService(models.Model):
    title=models.CharField(
        max_length=200
    )
    description=models.TextField()
    image=models.ImageField(
        upload_to='events/',
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

class EventMenu(models.Model):
    event=models.ForeignKey(
        EventService,
        on_delete=models.CASCADE,
        related_name='event_menus'
    )
    menu_item=models.ForeignKey(
        'menu.MenuItem',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return f"{self.event.title}"


class EventPackage(models.Model):
    event=models.ForeignKey(
        EventService,
        on_delete=models.CASCADE,
        related_name='event_packages'
    )
    package=models.ForeignKey(
        OfferPackage,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.event.title}"