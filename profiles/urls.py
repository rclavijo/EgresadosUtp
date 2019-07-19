from django.urls import path, re_path
from .views import ProfileListView, ProfileDetailView, agregar, eliminar

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
    path('agregar/<profile>/',agregar, name='agregar'),
    path('eliminar/<user>/',eliminar, name='eliminar'),
], "profiles")
