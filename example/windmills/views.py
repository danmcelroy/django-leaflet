import json
from django.shortcuts import render
from .models import Windmill

def index(request):
    #windmills = Windmill.objects.all()
    windmills1 = list(Windmill.objects.all().values('title', 'latitude', 'longitude'))
    return render(request,'windmills/index.html',{'windmills': windmills1})
