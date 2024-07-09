from django.contrib.auth.models import User
from .models import Game
from rest_framework import status
from rest_framework.test import APITestCase


class GameListAdminViewTests(APITestCase):
    def setUp(self):
        password = 'pass'
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.client.login(username=my_admin.username, password=password)

    def test_can_list_games(self):
        admin = User.objects.get(username='myuser')
        Game.objects.create(owner=admin, title='a title')
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    

class GameListUserViewTests(APITestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='matt', password='pass')
        

    def test_cannot_list_games(self):
        user = User.objects.get(username='matt')
        Game.objects.create(owner=user, title='a title')
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print(response.data)
        print(len(response.data))
        
