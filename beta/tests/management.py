"""
Beta app management command tests.
"""

from django.core import mail
from django.core.management import call_command

from django.test import TestCase
from beta import models


class SendInvitations(TestCase):
    """
    Test sending email invitations.
    """

    def setUp(self):
        """
        Add some random beta testers
        """
        super(SendInvitations, self).setUp()

        invites = [
            models.Beta(
                name='James',
                email='james@example.com'),
            models.Beta(
                name='Greg',
                email='greg@example.com'),
            models.Beta(
                name='Brian',
                email='brian@example.com',
                priority=True),
            models.Beta(
                name='Cannonball',
                email='julian@example.com'),
            models.Beta(
                name='Trane',
                email='trane@example.com'),
            models.Beta(
                name='John',
                email='john@example.com',
                priority=True)
        ]

        models.Beta.objects.bulk_create(invites)

    def test_priority(self):
        """
        Test that a user with the "priority" flag set receive an
        invitation when they are not at the top of the list.
        """
        # both priority people should get an invite.
        call_command('send_invitations', 2)

        invites = models.Beta.objects.exclude(invite_hash=None)

        self.assertEquals(invites.count(), 2)
        self.assertEquals(len(mail.outbox), 2)

    def test_message(self):
        """
        Make sure the person's name is in the email.
        """
        call_command('send_invitations', 2)

        self.assertEquals(len(mail.outbox), 2)

        self.assertEquals(mail.outbox[0].subject,
            u'Your invitation to our service!')

        self.assertTrue('Brian' in mail.outbox[0].body)
        self.assertTrue('John' in mail.outbox[1].body)
