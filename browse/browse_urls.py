from django.conf.urls import url
from browse import views

urlpatterns = [
    url(r'^show_information/', views.show_information),
]
