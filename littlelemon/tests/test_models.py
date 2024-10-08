from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def instance(self):
        return Menu.objects.create(title='Ice Cream', price=80, inventory=100)
    
    def test_get_item(self):
        item = self.instance()
        self.assertEqual(str(item), "Ice Cream : 80")

