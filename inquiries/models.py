from django.db import models


class Inquiry(models.Model):

    EVENT_CHOICES=[

        ('Wedding','Wedding'),
        ('Corporate','Corporate'),
        ('Birthday','Birthday'),
        ('Anniversary','Anniversary'),
        ('Holiday Party','Holiday Party'),
        ('Cultural/Religious Celebration','Cultural/Religious Celebration'),
        ('Other','Other')

    ]


    GUEST_CHOICES=[

        ('Under 25','Under 25'),
        ('25-50','25-50'),
        ('50-100','50-100'),
        ('100-200','100-200'),
        ('200+','200+')

    ]


    SERVICE_STYLE=[

        ('Buffet','Buffet'),
        ('Plated/Seated','Plated/Seated'),
        ('Family Style','Family Style'),
        ('Stations','Stations'),
        ('Cocktail/Appetizers','Cocktail/Appetizers'),
        ('Drop-off','Drop-off')

    ]


    LOCATION_TYPE=[

        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')

    ]


    STATUS_CHOICES=[

        ('New','New'),
        ('Pending','Pending'),
        ('Contacted','Contacted'),
        ('In Progress','In Progress'),
        ('Quote Sent','Quote Sent'),
        ('Confirmed','Confirmed'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled')

    ]


    HEAR_ABOUT_CHOICES=[

        ('','Select an option'),

        ('Google Search','Google Search'),
        ('Facebook','Facebook'),
        ('Instagram','Instagram'),
        ('YouTube','YouTube'),
        ('Friend / Family','Friend / Family'),
        ('Referral','Referral'),
        ('Advertisement','Advertisement'),
        ('Website','Website'),
        ('Other','Other')

    ]


    # CONTACT INFO

    full_name=models.CharField(
        max_length=100
    )

    email=models.EmailField()

    phone=models.CharField(
        max_length=20
    )

    company=models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    # EVENT DETAILS

    event_type=models.CharField(
        max_length=100,
        choices=EVENT_CHOICES
    )

    event_date=models.DateField()

    flexible_date=models.BooleanField(
        default=False
    )

    event_time=models.TimeField(
        blank=True,
        null=True
    )

    guests=models.CharField(
        max_length=50,
        choices=GUEST_CHOICES
    )

    venue=models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    indoor_outdoor=models.CharField(
        max_length=50,
        choices=LOCATION_TYPE,
        blank=True,
        null=True
    )


    # FOOD PREFERENCES

    cuisine=models.CharField(
        max_length=200
    )

    service_style=models.CharField(
        max_length=100,
        choices=SERVICE_STYLE,
        blank=True,
        null=True
    )

    dietary_requirements=models.TextField(
        blank=True,
        null=True
    )

    services_needed=models.TextField(
        blank=True,
        null=True
    )


    # BUDGET & DETAILS

    budget=models.CharField(
        max_length=100
    )

    event_details=models.TextField(
        blank=True,
        null=True
    )

    hear_about=models.CharField(
        max_length=100,
        choices=HEAR_ABOUT_CHOICES,
        blank=True,
        null=True
    )


    # ADMIN TRACKING

    status=models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )

    created=models.DateTimeField(
        auto_now_add=True
    )

    updated=models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return f"{self.full_name} - {self.event_type}"