from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):

    def test_create_item(self):
        item = ItemModel('Test Name', 19.99)
        self.assertEqual(item.name, 'Test Name', "Custom Error message in case the test fails: The name of the item is not equal to the constructor argument")
        self.assertEqual(item.price, 19.99)

    def test_item_json(self):
        item = ItemModel('Test Name', 19.99)
        expected = {
            'name': 'Test Name',
            'price': 19.99
        }
        self.assertEqual(item.json(), expected, "The JSON export of the item is incorrect. Received {}, expected {}".format(item.json(), expected))