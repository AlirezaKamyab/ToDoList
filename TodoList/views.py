from django.forms.fields import NullBooleanField
from django.shortcuts import render, redirect
from .models import List
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        AddItem(request.POST['itemName'])
        all_items = ShowLists()
        context = {'items':all_items}
        messages.success(request, 'Item added successfully!')
        return render(request, 'home.html', context)
    else:
        all_items = ShowLists()
        context = {'items':all_items}
        return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})

def delete(request, item_id):
    try:
        item = List.objects.get(pk=item_id)
        item.delete()
        messages.success(request, 'Item deleted successfully')
        return redirect('home')
    except:
        return redirect('home')

def crossout(request, item_id):
    try:
        item = List.objects.get(pk = item_id)
        item.changeChecked()
        item.save()
        messages.success(request, 'Item is checked!' if item.checked else 'item is unchecked!')
    except:
        pass
    finally:
        return redirect('home')