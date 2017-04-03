from django.shortcuts import render
from django.http import HttpResponse
import time


def index(request):
    hello = "Hello World! Today's date is: " 
    return HttpResponse(hello + time.strftime("%c") )
