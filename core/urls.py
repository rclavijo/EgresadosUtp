from django.urls import path
from .views import HomePageView,samplePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', samplePageView.as_view(), name="sample"),
]