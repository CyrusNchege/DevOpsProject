from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm
from .models import Item

# Create your views here.

def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item_detail.html', {'item': item})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', id=item.id)
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def edit_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', id=item.id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})

def delete_item(request, id):
    Item.objects.get(id=id).delete()
    return redirect('index')

