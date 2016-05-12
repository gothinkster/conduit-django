from django.conf.urls import url

from .views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]