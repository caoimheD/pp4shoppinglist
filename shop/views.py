from django.shortcuts import render, HttpResponse, redirect
from .models import Item

# Create your views here.


def home_page(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, '../templates/base.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('lists')
    return render(request, '../templates/add_item.html')


def your_lists(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, '../templates/shop_list.html', context)