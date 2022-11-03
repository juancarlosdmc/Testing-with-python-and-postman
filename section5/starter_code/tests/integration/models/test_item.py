from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)
            #assert that item does not exist before saving it to db
            self.assertIsNone(ItemModel.find_by_name('test'))

            item.save_to_db()
            # assert that item does exist AFTER saving it to db
            self.assertIsNotNone(ItemModel.find_by_name('test'), f"Found an item with name {item.name}, but expected not to.")

            item.delete_from_db()

            # assert that item does not exist after deleting from the db
            self.assertIsNone(ItemModel.find_by_name('test'))