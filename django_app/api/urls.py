from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^keyboard', views.KeyAPIView.as_view()),
    url(r'^message', views.CheckAPIView.as_view())
]









