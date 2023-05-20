from django.urls import path
from cryptage import views
urlpatterns = [
    path('',views.home)
]
