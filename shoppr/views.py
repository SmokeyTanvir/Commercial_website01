from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.conf import settings

# Create your views here.
def index(request):
	return render(request, "index.html", {
		"item": Item.objects.all()
		})


def showItem(request, item_name):
	return HttpResponse(f"kire {item_name}")