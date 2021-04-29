from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import  products_all


class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django_beginner', author='admin', description='django', created_by_id=1,
                                                slug='django-beginner', price=12, in_stock=True, is_active=True, image='django')
        User.objects.create(username='admin')

    def test_url_allowed_host(self):

        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse("store:product_detail", args=["django-beginner"]))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse("store:category_list", args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = products_all(request)
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title> BookStore </title>', html)
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertEqual(response.status_code, 200)

    def test_view_functions(self):
        request = self.factory.get('item/django-beginner')
        response = products_all(request)
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title> BookStore </title>', html)
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertEqual(response.status_code, 200)
