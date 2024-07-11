from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from games.models import Game

class TrendingListViewTests(APITestCase):
    def setUp(self):
        """
        Set up testing environment
        """
        password = 'pass'
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.client.login(username=my_admin.username, password=password)
        test_user = User.objects.create_user(username='matt', password='pass')


    
    def test_can_list_trending_posts(self):
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
        response = self.client.get('/trending/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))


class TrendingDetailViewTests(APITestCase):
    """
    Set up testing environment creating,
    test game, test post assigning the
    correct owners
    """
    def setUp(self):
        password = 'pass'
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        test_game = Game.objects.create(owner=my_admin, title='a title')
        matt = User.objects.create_user(username='matt', password='pass')
        Post.objects.create(owner=matt, title='a title', content='adams content', game=test_game)
        
    
    """
    Test to check if the user can retrieve a
    post by its id
    """
    def test_can_retrieve_trending_post_using_valid_id(self):
        response = self.client.get('/trending/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    




