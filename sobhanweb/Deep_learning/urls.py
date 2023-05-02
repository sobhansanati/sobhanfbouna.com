from django.urls import path
from . import views



app_name = 'Deep_learning'
urlpatterns = [
    #path('',AddEmail.as_view(),name='Home'),
    path('Deep_learning/',views.Deep_learning,name='Dl'),
]
