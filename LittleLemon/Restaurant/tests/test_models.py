from django.test import TestCase
from Restaurant.models import MenuItem
from Restaurant.serializers import MenuItemSerializer
from .constants import test_instances
import random

# test for menu items
class MenuItemTest(TestCase):
    def setUp(self):
        # setup a local database for testing
        for menu in test_instances:
            MenuItem.objects.create(title=menu["title"],
                                    price=menu["price"])

    def check_equal(self, item, instance_id):
        self.assertEqual(str(item), 
                         f"{test_instances[instance_id]['title']} : {test_instances[instance_id]['price']:.2f}")

    def test_get_item(self):
        # get a random instance and test its  
        id = random.randint(0, len(test_instances)-1) 
        item = MenuItem.objects.get(title=test_instances[id]["title"])
        self.check_equal(item, id)

    def test_get_all(self):
        items = MenuItem.objects.all()
        for id, item in enumerate(items):
            self.check_equal(item, id)