"""
Beta signup models.
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Beta(models.Model):
    """
    this model allows one to collect beta signup information.
    """
    name = models.CharField(_('name'), max_length=75)
    email = models.EmailField(_('email address'))
    is_invited = models.BooleanField(_('is invited'), default=False,
        help_text=_('Whether or not the user has been invited to '
                    'the system'))
    date_sent = models.DateTimeField(_('date sent'), blank=True, null=True,
        help_text=_('Date the invitation was sent.'))
    invite_hash = models.CharField(_('invitation hash'), max_length=36,
        blank=True, null=True,
        help_text=_('Unique hash sent in an email to a user when they '
                    'have been invited to the system.'))
    priority = models.BooleanField(_('priority'), default=False,
        help_text=_('If a user should get priority to be in '
                    'the next group invited regardless of their place '
                    'in line.'))
    claimed = models.BooleanField(_('claimed'),
        default=False,
        help_text=_('Whether or not the invitation has been claimed'))

    class Meta:
        """ Define ordering, etc. """
        verbose_name = _('Beta signup')
        verbose_name_plural = _('Beta signups')
        ordering = ('-date_sent', )

    def __unicode__(self):
        return self.name
