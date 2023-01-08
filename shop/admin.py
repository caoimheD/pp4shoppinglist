from django.contrib import admin
from .models import List, Item, ShoppingItem, ItemsBuy

# Register your models here.
admin.site.register(List)
admin.site.register(Item)
admin.site.register(ShoppingItem)
admin.site.register(ItemsBuy)