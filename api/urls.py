
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('users/', include('users.urls')),
    path('image/', include('image.urls'))
]
