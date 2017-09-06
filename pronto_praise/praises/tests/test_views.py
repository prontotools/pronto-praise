from django.core.urlresolvers import reverse
from django.test import TestCase


class PraiseListView(TestCase):
    def test_praise_list_view_should_be_accessible(self):
        response = self.client.get(reverse('praise_list'))
        self.assertEqual(response.status_code, 200)
