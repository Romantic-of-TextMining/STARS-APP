import unittest
from flask import current_app
from app import create_app, db


class ServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_text_cloud_generate_img(self):
        from app.main import text_cloud
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, '../../../app/static/assets/data.json')
        new_text_cloud = text_cloud.AddTextCloud(path)
        new_text_cloud.create_textcloud()
        #check img
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

