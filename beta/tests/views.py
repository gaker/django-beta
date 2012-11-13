# beta/tests/views.py

from django.core.urlresolvers import reverse
from django.test import TestCase

from beta.models import Beta


class SignUp(TestCase):
    """
    Test signing up for the beta.
    """

    def test_user_signup(self):
        """
        Test a successful user signup.
        """
        initial_count = Beta.objects.all().count()

        url = reverse('beta-signup')

        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

        data = {
            'name': 'Mr Splashy Pants',
            'email': 'mr@splashypants.com'
        }

        resp = self.client.post(url, data)

        self.assertEquals(resp.status_code, 302)
        self.assertEquals(
            Beta.objects.all().count(),
            initial_count + 1)

        invite = Beta.objects.get(email='mr@splashypants.com')

        self.assertEquals(invite.name, 'Mr Splashy Pants')

    def test_duplicate_signup(self):
        """
        Test a form valdation exception is thrown if a user tries
        to sign up multiple times.
        """
        url = reverse('beta-signup')
        data = {
            'name': 'Miles Davis',
            'email': 'miles@example.com'
        }
        resp = self.client.post(url, data)

        self.assertEquals(resp.status_code, 302)

        resp = self.client.post(url, data)
        self.assertEquals(resp.status_code, 200)
