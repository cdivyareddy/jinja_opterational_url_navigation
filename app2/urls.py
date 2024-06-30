from django.urls import path
from app2.views import *
app_name='charanc'

urlpatterns=[
    path('charan/',charan,name='charan')
]