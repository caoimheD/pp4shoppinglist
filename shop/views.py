from django.shortcuts import render, HttpResponse

# Create your views here.


def get_list(request):
    return render(request, '../templates/shop_list.html')
