from django.urls import path
from cryptage import views
urlpatterns = [
    path('',views.home,name="home"),
    path('list/',views.list,name='list')

]
