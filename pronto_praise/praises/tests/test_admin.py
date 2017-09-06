from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Praise


class PraiseAdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'admin@pronto.com', 'admin')
        self.client.login(username='admin', password='admin')

        self.url = '/admin/praises/praise/'

    def test_access_praise_admin_should_have_columns(self):
        Praise.objects.create(
            to='Mils',
            by='Kan',
            description='Great work! Thanks for your patience.'
        )
        response = self.client.get(self.url)

        expected = '<div class="text"><a href="?o=1">To</a></div>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<div class="text"><a href="?o=2">By</a></div>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<div class="text"><a href="?o=3">Description</a></div>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<div class="text"><a href="?o=4">Created</a></div>'
        self.assertContains(response, expected, count=1, status_code=200)
