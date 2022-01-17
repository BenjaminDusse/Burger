from django.urls import path, include


urlpatterns = [
    path('menu/', include(('burger.urls', 'burger'), 'burger')),
]