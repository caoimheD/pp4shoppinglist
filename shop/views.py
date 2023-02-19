from django.shortcuts import render, HttpResponse, redirect
from .models import List, Item
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


def home_page(request):
    return render(request, '../templates/base.html')

# Views for lists


class CreateList(LoginRequiredMixin, CreateView):
    model = List
    fields = 'title', 'description', 'dueDate', 'complete'
    template_name = '../templates/create_list.html'

    def get_success_url(self):
        return reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'List created successfully!')
        return super(CreateList, self).form_valid(form)


class ShopList(LoginRequiredMixin, ListView):
    model = List
    template_name = '../templates/shop_list.html'
    context_object_name = 'shoppinglists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppinglists'] = \
            context['shoppinglists'].filter(user=self.request.user)
        return context


class ListDetail(LoginRequiredMixin, DetailView):
    model = List
    template_name = '../templates/shop_detail.html'
    context_object_name = 'listdetails'


class UpdateList(LoginRequiredMixin, UpdateView):
    model = List
    fields = 'title', 'description', 'dueDate', 'complete',
    template_name = '../templates/update_list.html'
    context_object_name = 'updatelist'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'List updated successfully!')
        return super(UpdateList, self).form_valid(form)


class DeleteList(LoginRequiredMixin, DeleteView):
    model = List
    template_name = '../templates/delete_list.html'

    def get_success_url(self):
        return reverse_lazy('lists')

    def form_valid(self, form):
        messages.success(self.request, 'List deleted successfully!')
        return super(DeleteList, self).form_valid(form)

# Views for items


class CreateItem(LoginRequiredMixin, CreateView):
    model = Item
    fields = 'name', 'quantity',
    template_name = '../templates/additem.html'
    context_object_name = 'create'

    def form_valid(self, form):
        form.instance.list = List.objects.get(pk=self.kwargs['pk'])
        messages.success(self.request, 'Item created successfully!')
        return super(CreateItem, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.kwargs['pk']})


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = '../templates/delete_item.html'

    def form_valid(self, form):
        self.list_pk = self.get_object().list.pk
        messages.success(self.request, 'Item deleted successfully!')
        return super(DeleteItem, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.list_pk})
