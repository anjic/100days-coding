from rest_framework import status
from rest_framework.test import APITestCase
from api.models.sangroup_models import SanGroup

class SangroupTest(APITestCase):
# 
    def test_create_sangroup(self):
        data = {"sangroup_name":"fun","comment":"","modified_by":"1","created_by":"1","sangroup_id":""}
        response = self.client.post('/api/sangroup/', data, format='json')
        assert (response.status_code == status.HTTP_201_CREATED)

    def test_get_sangroup_list(self):
        response = self.client.get('/api/sangroup/', format='json')
        assert(response.status_code == (status.HTTP_200_OK or status.HTTP_301_MOVED_PERMANENTLY))

    def test_get_sangroup(self):
        response = self.client.get('/api/sangroup/1/', format='json')
        assert(response.status_code == (status.HTTP_200_OK or status.HTTP_301_MOVED_PERMANENTLY))

    def test_get_sangroup_neg(self):
        response = self.client.get('/api/user/8/', format='json')
        assert (response.status_code == status.HTTP_404_NOT_FOUND)

    def test_update_sangroup(self):
        data = {"sangroup_name":"fun","comment":"","modified_by":"1","created_by":"1","sangroup_id":""}
        response = self.client.put('/api/sangroup/2/', data, format = 'json')
        assert (response.status_code == status.HTTP_200_OK)

    def test_update_sangroup_neg(self):
        data = {"sangroup_name":"test"}
        response = self.client.put('/api/sangroup/1/', data, format = 'json')
        assert (response.status_code == status.HTTP_400_BAD_REQUEST)

    def test_delete_sangroup(self):
        response = self.client.delete('/api/sangroup/2/')
        assert(response.status_code == status.HTTP_204_NO_CONTENT)

    def test_delete_sangroup_present(self):
        response = self.client.delete('/api/sangroup/1/')
        assert(response.status_code == status.HTTP_400_BAD_REQUEST)

    def test_delete_sangroup_neg(self):
        response = self.client.delete('/api/sangroup/20/')
        assert(response.status_code == status.HTTP_404_NOT_FOUND)