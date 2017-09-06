from django.test import TestCase

from ..models import Praise


class PraiseTest(TestCase):
    def test_save_praise(self):
        praise = Praise()
        praise.to = 'Mils'
        praise.by = 'Kan'
        praise.description = 'Great work! Thanks for your patience.'
        praise.save()

        praise = Praise.objects.last()

        self.assertEqual(praise.to, 'Mils')
        self.assertEqual(praise.by, 'Kan')
        self.assertEqual(
            praise.description,
            'Great work! Thanks for your patience.'
        )
        self.assertTrue(praise.created)
