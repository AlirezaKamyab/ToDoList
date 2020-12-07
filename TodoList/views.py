from django.shortcuts import render
from .models import List

# Create your views here.
def home(request):
    all_items = List.objects.all()
    context = {'items':all_items}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})
