from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post
from games.models import Game
from .models import Comment

class CommentListViewTests(APITestCase):
    def setUp(self):
        """
        Set up testing environment
        """
        password = 'pass'
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        test_game = Game.objects.create(owner=my_admin, title='a title')
        matt = User.objects.create_user(username='matt', password='pass')
        test_post = Post.objects.create(owner=matt, title='a title', content='matts content', game=test_game)


    
    def test_can_list_comments(self):
        """
        Test that gets the admin user, which
        then creates a game, which then allows
        a user to select the game id, create
        a post, then create a comment
        """
        my_admin = User.objects.get(username='myuser')
        test_game = Game.objects.create(owner=my_admin, title='a title')
        matt = User.objects.get(username='matt')
        test_post = Post.objects.create(owner=matt, title='a title', content='matts content', game=test_game)
        Comment.objects.create(owner=matt, post=test_post, content='hi')
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))



class CommentDetailViewTests(APITestCase):
    def setUp(self):
        password = 'pass'
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        test_game = Game.objects.create(owner=my_admin, title='a title')
        matt = User.objects.create_user(username='matt', password='pass')
        test_post= Post.objects.create(owner=matt, title='a title', content='matts content', game=test_game)
        Comment.objects.create(owner=matt, post=test_post, content='some content')
        

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'some content')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    




    


