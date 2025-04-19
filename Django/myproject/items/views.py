# items/views.py

from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def homepage(request):
    items = Item.objects.all()  # Fetch all items from the database
    return render(request, 'items/homepage.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ItemForm()
    return render(request, 'items/add_item.html', {'form': form})
