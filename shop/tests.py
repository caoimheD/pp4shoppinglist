from django.test import TestCase
from .models import List, Item
from django.contrib.auth.models import User


class TestModels(TestCase):
    def test_compete_defaults_to_false(self):
        list = List.objects.create(title='Test', user=User.objects.create(username="test", password="test"), description='test', list_items='test')
        self.assertFalse(list.complete)
