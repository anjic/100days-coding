from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserTest(APITestCase):
    def test_create_user(self):
        data = {"username": "jerryelli", "first_name": "tom", "last_name": "jerry", "email": "tommy@gmail.com",
                "password": "password", "confirmpassword": "password", "modified_by": "1", "created_by": "1", "id": "",
                "is_active": True, "is_staff": True, "group_id": "2"}
        response=self.client.post('/api/user/', data, format = 'json')
        assert (response.status_code == status.HTTP_201_CREATED)

    def test_create_user_neg(self):
        data = {"first_name": "tom", "last_name": "jerry", "email": "tommy@gmail.com",
                "password": "password", "confirmpassword": "password", "modified_by": "1", "created_by": "1", "id": "",
                "is_active": True, "is_staff": True, "group_id": "2"}
        response = self.client.post('/api/user/', data, format = 'json')
        assert (response.status_code == status.HTTP_400_BAD_REQUEST)

    def test_get_user_list(self):
        response = self.client.get('/api/user/', format='json')
        assert(response.status_code == (status.HTTP_200_OK or status.HTTP_301_MOVED_PERMANENTLY))
        # self.assertEqual(User.objects.count(), 5)
        # self.assertEqual(User.objects.get(id=1).first_name, 'divya')
        # print(self.client.get('/api/user/1'))

    def test_get_user(self):
        response = self.client.get('/api/user/18/', format='json')
        assert (response.status_code == (status.HTTP_200_OK or status.HTTP_301_MOVED_PERMANENTLY))
        # self.assertEqual(User.objects.count(), 5)
        # self.assertEqual(User.objects.get(id=1).first_name, 'divya')
        # print(self.client.get('/api/user/1'))

    def test_get_user_neg(self):
        response = self.client.get('/api/user/2/', format='json')
        assert (response.status_code == status.HTTP_404_NOT_FOUND)
        # self.assertEqual(User.objects.count(), 5)
        # self.assertEqual(User.objects.get(id=1).first_name, 'divya')
        # print(self.client.get('/api/user/1'))

    def test_update_user(self):
        data = {"first_name":"jerry","username":"msys"}
        response = self.client.put('/api/user/18/', data, format = 'json')
        assert (response.status_code == status.HTTP_200_OK)

    def test_update_user_neg(self):
        data = {"first_name":"text"}
        response = self.client.put('/api/user/18/', data, format = 'json')
        assert (response.status_code == status.HTTP_400_BAD_REQUEST)

    def test_delete_user(self):
        response = self.client.delete('/api/user/18/')
        assert(response.status_code == status.HTTP_204_NO_CONTENT)

    def test_delete_user_neg(self):
        response = self.client.delete('/api/user/2/')
        assert(response.status_code == status.HTTP_404_NOT_FOUND)
