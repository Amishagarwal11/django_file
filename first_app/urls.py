from django.urls import path
from first_app import views

urlpatterns=[
    path('',views.show,name='first_app')
]