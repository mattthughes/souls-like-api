from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from games.models import Game

class PostListViewTests(APITestCase):
    def setUp(self):
        """
        Set up testing environment
        """
        password = 'pass'
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.client.login(username=my_admin.username, password=password)
        test_user = User.objects.create_user(username='matt', password='pass')


    
    def test_can_list_posts(self):
        """
        Test that gets the admin user, which
        then creates a game, which then allows
        a user to select the game id, create
        a post
        """
        admin = User.objects.get(username='myuser')
        test_game = Game.objects.create(owner=admin, title='a title')
        matt = User.objects.get(username='matt')
        Post.objects.create(owner=matt, title='a title', game=test_game)
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

