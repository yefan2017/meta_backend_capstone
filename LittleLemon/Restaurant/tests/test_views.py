from django.test import TestCase
from .constants import test_instances
from Restaurant.models import MenuItem
from Restaurant.views import MenuItemsView
from django.http import HttpRequest 

class MenuViewTest(TestCase): 
    def setUp(self):
        # setup a local database for testing
        for menu in test_instances:
            MenuItem.objects.create(title=menu["title"],
                                    price=menu["price"])
    
    def test_item_view(self): 
        # check view returned information correctness 
        request = HttpRequest()
        request.method="GET"
        response = MenuItemsView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        for item in response.data:
            item_dict = {"title": item["title"], "price": float(item["price"])}
            self.assertTrue(item_dict in test_instances)