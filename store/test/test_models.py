from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoryModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name='django',slug='django')


    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data,Category))

    def test_category_model_return_string(self):
        data = self.data1
        self.assertEquals(str(data), 'django')

class TestProductModel(TestCase):


    def setUp(self):
        self.data1 = Category.objects.create(name='django',slug='django')
        self.data1 = Product.objects.create(category_id=1,title='django_beginner',author='admin', description='django',created_by_id=1,
                                                slug='django-beginner',price=12,in_stock=True,is_active=True)
        User.objects.create(username='admin')


    def test_product_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))

    def test_product_model_return_string(self):
        data = self.data1

        self.assertEquals(str(data),'django_beginner')
    
