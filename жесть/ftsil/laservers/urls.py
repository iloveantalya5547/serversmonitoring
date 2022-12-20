from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'servers_home'),
    path('<int:pk>', views.onebyone.as_view(), name ='server-detail')
]