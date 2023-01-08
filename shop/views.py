from django.shortcuts import render, HttpResponse, redirect
from .models import List, Item, ShoppingItem, ItemsBuy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import ListForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.


def home_page(request):
    return render(request, '../templates/base.html')


# Views for lists


class CreateList(CreateView):
    model = List
    fields = 'title', 'description', 'date', 'list_items', 'items', 'complete'
    template_name = '../templates/create_list.html'

    def get_success_url(self):
        return reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateList, self).form_valid(form)


class ShopList(ListView):
    model = List
    template_name = '../templates/shop_list.html'
    context_object_name = 'shoppinglists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppinglists'] = context['shoppinglists'].filter(user=self.request.user)
        return context


class ListDetail(DetailView):
    model = List
    template_name = '../templates/shop_detail.html'
    context_object_name = 'listdetails'


class UpdateList(UpdateView):
    model = List
    fields = 'title', 'description', 'date', 'complete',
    template_name = '../templates/update_list.html'
    context_object_name = 'updatelist'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.pk})


class DeleteList(DeleteView):
    model = List
    template_name = '../templates/delete_list.html'

    def get_success_url(self):
        return reverse_lazy('lists')

# Views for items

"""
class ItemList(ListView):
    model = ItemsBuy
    template_name = '../templates/shop_detail.html'
    context_object_name = 'itemslist'


class ItemDetail(DetailView):
    model = ItemsBuy
    template_name = '../templates/shop_detail.html'
    context_object_name = 'items'


"""


class AddItems(UpdateView):
    model = List
    fields = 'list_items',
    template_name = '../templates/add_item.html'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.pk})

