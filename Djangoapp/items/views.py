from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'items/item_list.html', {'items': items, 'form': form})
