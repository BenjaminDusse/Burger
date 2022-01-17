from django.urls import path
from burger.views import BurgerListView


urlpatterns = [
    path("", BurgerListView.as_view(), name="burger_list"),
]