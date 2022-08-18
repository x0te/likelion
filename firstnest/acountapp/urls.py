from django.urls import path
from acountapp.views import hello_world

app_name = "accountapp"
urlpatterns = [
    path('hello_world/', hello_world, name='hello world')
]
    