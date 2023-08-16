from django.test import TestCase
from .models import MenuItem
from .serializers import MenuItemSerializer
import random

test_instances = [
    { "title" : "IceCream", "price" : 20},
    { "title" : "Grilled Salmon", "price" : 80},
    { "title" : "Chicken Fajita", "price" : 60},
    { "title" : "Beef Burrito", "price" : 15},
]

# test for menu items
class MenuItemTest(TestCase):
    def setUp(self):
        # setup a local database
        for menu in test_instances:
            MenuItem.objects.create(title=menu["title"],
                                    price=menu["price"])

    def check_equal(self, item, instance_id):
        self.assertEqual(str(item), 
                         f"{test_instances[instance_id]['title']} : {test_instances[instance_id]['price']:.2f}")

    def test_get_item(self):
        # get a random instance and test its  
        id = random.randint(0, len(test_instances)) 
        item = MenuItem.objects.get(title=test_instances[id]["title"])
        self.check_equal(item, id)

    def test_get_all(self):
        items = MenuItem.objects.all()
        for id, item in enumerate(items):
            self.check_equal(item, id)