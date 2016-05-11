from django.conf.urls import url

from .views import RegistrationAPIView

urlpatterns = [
    url(r'^users/?$', RegistrationAPIView.as_view()),
]