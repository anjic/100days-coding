from django.test import TestCase
from xio_ise.settings import INSTALLED_APPS
# Create your tests here.
class SettingsTest(TestCase):    
    def test_api_is_configured(self):
        assert 'api.apps.ApiConfig' in INSTALLED_APPS