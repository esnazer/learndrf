from django.test import TestCase
from shop.models import Categorial, Product

class BasicTest(TestCase):
    
    #Configurar parametros de base de datos
    def setUp(self):
        Categorial.objects.create(name='categoria1')
        Categorial.objects.create(name='categoria2')
        Product.objects.create(name='producto1', price=123, stock=24, image_url='some')
        Product.objects.create(name='producto2', price=6345, stock=3, image_url='some')
        return super().setUp()
    
class ShopProduct(BasicTest):
    def testListProduct(self):
        products = Product.objects.all()
        self.assertIn('producto1', products.values_list('name', flat=True))
        self.assertIn('producto2', products.values_list('name', flat=True))

    def testFilterProduct(self):
        producto1 = Product.objects.filter(name='producto1')
        self.assertEqual(producto1[0].name, 'producto1')
        

class ShopCategorial(BasicTest):
    def testListCategorial(self):
        pass