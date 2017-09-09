from django.core.urlresolvers import reverse
from django.test import TestCase
from praises.models import Praise


class PraiseListView(TestCase):
    def test_praise_list_view_should_be_accessible(self):
        response = self.client.get(reverse('praise_list'))
        self.assertEqual(response.status_code, 200)

    def test_praise_list_view_should_have_title_saying_pronto_praise(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<title>Pronto Praise</title>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_list_view_should_use_jquery_and_semantic_ui(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<link rel="stylesheet" type="text/css" ' \
            'href="/static/semantic/semantic.min.css">'
        self.assertContains(response, expected, status_code=200)
        expected = '<script\n    src="https://code.jquery.com/' \
            'jquery-3.1.1.min.js"\n    ' \
            'integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDY' \
            'GmIJLv2b8="\n    crossorigin="anonymous"></script>'
        self.assertContains(response, expected, status_code=200)
        expected = '<script src="/static/semantic/semantic.min.js"></script>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_list_view_should_have_header_saying_praise(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<h1 class="ui header" style="display:inline-block">Praise</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_list_view_should_have_praise_with_info_as_expected(self):
        Praise.objects.create(
            to='chang',
            by='o',
            description='GGwp:angry:',
            number_of_hearts=1000
        )
        response = self.client.get(reverse('praise_list'))

        self.assertContains(response, 'chang', status_code=200)
        self.assertContains(response, 'o', status_code=200)
        self.assertContains(response, 'GGwp', status_code=200)
        self.assertContains(response, 1000, status_code=200)
        self.assertContains(
            response,
            '<img src="/static/emoji/img/angry.png"',
            status_code=200
        )

    def test_praise_list_view_should_have_add_button(self):
        response = self.client.get(reverse('praise_list'))
        expected = '<a href="/add" class="ui basic button' \
            '  right floated" ><i class="icon plus"></i>\n' \
            '          Praise Someone\n      </a>'
        self.assertContains(response, expected, status_code=200)


class PraiseAddView(TestCase):
    def test_praise_add_view_should_be_accessible(self):
        response = self.client.get(reverse('praise_add'))
        self.assertEqual(response.status_code, 200)

    def test_praise_add_view_should_have_header_saying_write_praise(self):
        response = self.client.get(reverse('praise_add'))

        expected = '<h1 class="ui header">Write your Praise :)</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_add_view_should_have_write_praise_form(self):
        response = self.client.get(reverse('praise_add'))

        expected = '<form class="ui form" method="post" action=".">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value='
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="text" name="to" ' \
            'placeholder="Whom do you want to write to?">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="text" name="by" placeholder="Pim Ch">'
        self.assertContains(response, expected, status_code=200)

        expected = '<textarea name="description"></textarea>'
        self.assertContains(response, expected, status_code=200)

        expected = '<button class="ui button" type="submit">Submit</button>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_add_view_should_add_new_praise(self):
        data = {
            'to': 'Por',
            'by': 'Poon',
            'description': 'Think'
        }
        response = self.client.post(reverse('praise_add'), data=data)
        self.assertEquals(response.status_code, 302)


class AddHeartView(TestCase):
    def test_add_heart_should_increase_number_of_heart(self):
        praise = Praise.objects.create(
                to="test",
                by="bytest",
                description="hearttest"
            )

        self.assertEqual(0, praise.number_of_hearts)
        response = self.client.get(
            reverse('praise_add_heart', kwargs={'praise_id': praise.id})
        )
        self.assertEqual(response.status_code, 302)
        praise = Praise.objects.get(id=praise.id)

        self.assertEqual(1, praise.number_of_hearts)
