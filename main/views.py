from django.shortcuts import render
from .models import Tower
# Create your views here.


def home(request):
    tower = Tower.objects.first()
    level = tower.level
    updated_at = tower.updated
    return render(request, 'home.html', {'level': level,'updated_at': updated_at})