"""
Beta form(s)
"""
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Beta


class BetaSignupForm(forms.ModelForm):
    """
    Beta user signup form
    """

    class Meta:
        """ Define model, etc. """
        model = Beta
        fields = ('name', 'email', )

    def clean_email(self):
        """
        See if the email address already exists in the
        system or not.
        """
        value = self.cleaned_data['email']
        try:
            Beta.objects.get(email=value)

            raise forms.ValidationError(
                _('A submission for this email address already exists.'))
        except Beta.DoesNotExist:
            return value
