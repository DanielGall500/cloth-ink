from django.shortcuts import render
from django.views import generic
from service.models import Item

# Create your views here.
class ItemView(generic.ListView):
	model = Item
	template_name = 'service/index.html'