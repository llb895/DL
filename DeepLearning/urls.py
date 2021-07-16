from django.conf.urls import url
from DeepLearning import views

urlpatterns = [
    url(r'^submitcomment/', views.submitcomment),
    url(r'^show_books/', views.show_books),
]
