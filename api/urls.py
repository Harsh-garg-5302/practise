from django.urls import path
from .views import LoginApiView, CarModelViewSet, SignupView

urlpatterns = [
    path('studentapi', CarModelViewSet.as_view({'get': 'list'})),
    path('login', LoginApiView.as_view()),
    path('signup', SignupView.as_view()),
]