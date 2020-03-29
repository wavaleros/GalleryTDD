from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image, PortfolioCollection
import json

# Create your tests here.
class GalleryTestCase(TestCase):

    def test_list_images_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data),2)

    def test_verify_first_from_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)

        self.assertEqual(current_data[0]['fields']['name'],"nuevo")

    def test_add_user(self):
        response=self.client.post('/gallery/addUser/',json.dumps({"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5", "email": "test@test.com"}), content_type='application/json')
        current_data=json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'],'testUser')

    def test_list_portfolios(self):
        url = '/gallery/portfolios'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_specific_portfolio_amount(self):
        portfolio1 = PortfolioCollection()
        portfolio1.name = 'portfolio1'
        portfolio2 = PortfolioCollection()
        portfolio2.name = 'portfolio2'
        portfolio1.save()
        portfolio2.save()
        url = '/gallery/portfolios'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 2)

    def test_list_public_portfolio(self):
        portfolio1 = PortfolioCollection()
        portfolio1.name = 'portfolio3'
        portfolio1.public = True
        portfolio2 = PortfolioCollection()
        portfolio2.name = 'portfolio4'
        portfolio2.public = False
        portfolio1.save()
        portfolio2.save()

        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')

        Image.objects.create(name='nuevaImg', url='No', description='testImage', type='jpg', user=user_model,
                             portfolio=portfolio1, public=True)
        Image.objects.create(name='nuevaImg2', url='No', description='testImage', type='jpg', user=user_model,
                             portfolio=portfolio1, public=False)
        Image.objects.create(name='nuevaImg3', url='No', description='testImage', type='jpg', user=user_model,
                             portfolio=portfolio1, public=True)
        Image.objects.create(name='nuevaImg4', url='No', description='testImage', type='jpg', user=user_model,
                             portfolio=portfolio2, public=True)


        url = '/gallery/public-portfolios'
        response = self.client.get(url, {'idusuario': user_model.id}, format='json')
        self.assertEqual(response.status_code, 200)
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 2)


    def test_login(self):
        user_model = User.objects.create_user(username='testlogin', password='abcd-login', first_name='test', last_name='login', email='testlogin@test.com')

        response=self.client.post('/gallery/user/login/',json.dumps({"username": user_model.username, "password": user_model.password}), content_type='application/json')
        current_data=json.loads(response.content)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(current_data[0]['fields']['id'],user_model.id)
