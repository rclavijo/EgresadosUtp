from django.urls import path, re_path, include
from .views import pageListView,pageDetailView, PageCreate, PageUpdate

pages_patterns = ([
    path('', pageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', pageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
], 'pages')