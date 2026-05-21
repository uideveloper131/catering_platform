from django.urls import path
from .views import *

urlpatterns=[

    path(
        '',
        brands,
        name='brands'
    ),

    path(
        '<int:id>/',
        brand_detail,
        name='brand_detail'
    )

]