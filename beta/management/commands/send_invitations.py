# beta/managements/commands/send_invitations.py

from uuid import uuid4
from optparse import make_option

from django.conf import settings
from django.contrib.sites.models import Site
from django.core import mail
from django.core.urlresolvers import reverse
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils import timezone

from beta.models import Beta


class Command(BaseCommand):
    """
    This management command sends invitation emails.
    """

    args = '<num_invitations>'
    help = 'Send invitation emails'

    option_list = BaseCommand.option_list + (
        make_option('--signup-view',
            default='sign-up',
            dest='view',
            help="View name to send signups to."
        ),
    )

    def handle(self, *args, **options):
        """

        """
        if not args:
            num = settings.INVITATION_BATCH
        else:
            num = args[0]

        invites = Beta.objects\
            .filter(Q(is_invited=False) | Q(priority=True))\
            .order_by('-priority', 'pk')[:num]

        # open the SMTP connection once.
        connection = mail.get_connection()
        connection.open()

        with transaction.autocommit():
            subject = render_to_string('beta/invitation-subject.txt')\
                .strip('\n')

            url = 'http://{0}'.format(Site.objects.get_current().domain)
            for invite in invites:

                hash_exists = False
                while not hash_exists:
                    hash_ = str(uuid4())
                    try:
                        Beta.objects.get(invite_hash=hash_)
                    except Beta.DoesNotExist:
                        invite.invite_hash = hash_
                        hash_exists = True

                ctx = {
                    'invite': invite,
                    'url': '{0}{1}'.format(
                        url, reverse(options['view'], kwargs={'hash': hash_}))
                }
                message = render_to_string('beta/invitation-email.txt', ctx)\
                    .strip('\n')

                email = mail.EmailMessage(
                    subject=subject, body=message,
                    to=[invite.email], connection=connection
                )
                email.send()

                invite.date_sent = timezone.now()
                invite.is_invited = True
                invite.save()

        connection.close()

        self.stdout.write('%s invitations sent!' % invites.count())
