from django.urls import path
from .views import pageListView,pageDetailView, PageCreate, PageUpdate

pages_patterns = ([
    path('', pageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', pageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    
], 'pages')