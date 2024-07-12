from django.contrib.auth.models import User
from .models import Game
from rest_framework import status
from rest_framework.test import APITestCase


class GameListAdminViewTests(APITestCase):
    def setUp(self):
        """
        Creating a test environment
        and creating the admin user and logging
        them in
        """
        password = 'pass'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        self.client.login(username=my_admin.username, password=password)

    def test_can_list_games(self):
        """
        Testing that the admin user can access
        the game list view by assigning the owner
        to the admin user and checking the status
        code to make sure it returns 200 ok
        """
        admin = User.objects.get(username='myuser')
        Game.objects.create(owner=admin, title='a title')
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))


class GameListUserViewTests(APITestCase):
    def setUp(self):
        """
        Creating the test environment
        creating a test user
        """
        test_user = User.objects.create_user(username='matt', password='pass')

    def test_cannot_list_games(self):
        """
        Testing that the user cannot access
        the game list view by assigning the owner
        to the test user and checking the status
        code to make sure it returns 403 forbidden
        """
        user = User.objects.get(username='matt')
        Game.objects.create(owner=user, title='a title')
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print(response.data)
        print(len(response.data))


class GameDetailAdminViewTests(APITestCase):
    def setUp(self):
        """
        Set up testing environment creating the
        admin user and logging them in
        """

        password = 'pass'
        my_admin = User.objects.create_superuser(
            'myuser', 'myemail@test.com', password)
        self.client.login(username=my_admin.username, password=password)

    def test_can_retrive_game_using_valid_id(self):
        """
        Test to check if the user can retrieve a
        game by its id
        """
        admin = User.objects.get(username='myuser')
        Game.objects.create(owner=admin, title='a title')
        response = self.client.get('/games/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GameDetailUserViewTests(APITestCase):
    def setUp(self):
        """
        Setting up testing environment creating
        the test user
        """

        test_user = User.objects.create_user(username='matt', password='pass')

    def test_cannot_retrive_game_using_valid_id(self):
        """
        Testing that the user cannot access
        the game detail view by assigning the owner
        to the test user and checking the status
        code to make sure it returns 403 forbidden
        """
        user = User.objects.get(username='matt')
        Game.objects.create(owner=user, title='a title')
        response = self.client.get('/games/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
