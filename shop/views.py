from django.shortcuts import render, HttpResponse, redirect
from .models import List
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import ListForm
from django.urls import reverse, reverse_lazy

# Create your views here.


def home_page(request):
    return render(request, '../templates/base.html')


class ShopList(ListView):
    model = List
    template_name = '../templates/shop_list.html'
    context_object_name = 'shoppinglists'


class ListDetail(DetailView):
    model = List
    template_name = '../templates/shop_detail.html'
    context_object_name = 'listdetails'


class UpdateList(UpdateView):
    model = List
    fields = 'title', 'description', 'date', 'list_items', 'complete'
    template_name = '../templates/update_list.html'
    context_object_name = 'updatelist'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.pk})


"""
class ListDetail(DetailView):
    model = List

def your_lists(request):
    lists = List.objects.all()
    context = {
        'lists': lists
    }
    return render(request, '../templates/shop_list.html', context)
"""

def add_list(request):
    if request.method == 'POST':
        name = request.POST.get('list_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('lists')
    
    return render(request, '../templates/add_list.html')


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('lists')
    return render(request, '../templates/add_item.html')


