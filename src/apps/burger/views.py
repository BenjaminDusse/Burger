from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from burger.models import Burger


class BurgerListView(ListView):
    model = Burger
    context_object_name = 'burgers'
    template_name = 'burger/menu.html'