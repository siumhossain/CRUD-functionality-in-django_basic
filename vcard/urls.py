from django.urls import path
from .import views

app_name = 'vcard'

urlpatterns = [
    path('',views.home,name='home')
]