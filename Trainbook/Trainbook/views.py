# Django views for Trainbook project.

from django.shortcuts import render_to_response
from datetime import datetime

def welcome(request):
    return render_to_response ('base.html')
