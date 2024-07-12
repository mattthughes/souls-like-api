from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post
from comments.models import Comment
from games.models import Game
from .models import Like


class LikeListViewTests(APITestCase):
    def setUp(self):
        """
        Set up testing environment
        """
        password = 'pass'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        matt = User.objects.create_user(username='matt', password='pass')

    def test_can_like_posts(self):
        """
        Test that gets the admin user, which
        then creates a game, which then allows
        a user to select the game id, create
        a post, then create a comment
        """
        my_admin = User.objects.get(username='myuser')
        test_game = Game.objects.create(owner=my_admin, title='a title')
        matt = User.objects.get(username='matt')
        test_post = Post.objects.create(
            owner=matt, title='a title',
            content='matts content', game=test_game
            )
        Like.objects.create(owner=matt, post=test_post)
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

        def test_can_like_comments(self):
            """
        Test that gets the admin user, which
        then creates a game, which then allows
        a user to select the game id, create
        a post, then create a comment, and
        assigns the like to the correct post
        by its id
        """
            my_admin = User.objects.get(username='myuser')
        test_game = Game.objects.create(owner=my_admin, title='a title')
        matt = User.objects.get(username='matt')
        test_post = Post.objects.create(
            owner=matt, title='a title',
            content='matts content', game=test_game
            )
        test_comment = Comment.objects.create(
            owner=matt,
            content='matts content', post=test_post
            )
        Like.objects.create(owner=matt, comment=test_comment)
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))


class LikeDetailViewTests(APITestCase):
    def setUp(self):
        """
        Creating Test environment to set up tests,
        create test game, and test post assigning
        the correct users
        """
        password = 'pass'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        test_game = Game.objects.create(owner=my_admin, title='a title')
        matt = User.objects.create_user(username='matt', password='pass')
        test_post = Post.objects.create(
            owner=matt, title='a title',
            content='matts content', game=test_game
            )
        Like.objects.create(owner=matt, post=test_post)

    def test_can_retrieve_like_using_valid_id(self):
        """
        Test to check if the user can retrieve a
        like by its id
        """
        response = self.client.get('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
