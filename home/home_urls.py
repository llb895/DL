from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^home_submit/', views.home_submit),
    url(r'^show/', views.show),
]