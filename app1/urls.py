from django.urls import path
from app1.views import *
app_name='divyac'

urlpatterns=[
    path('divya/',divya,name='divya'),
]