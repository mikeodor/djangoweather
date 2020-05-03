from django.urls import path
from weather import views as weather_view
urlpatterns=[
    path('', weather_view.index, name="home")
]