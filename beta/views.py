"""
Beta views.
"""

from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .forms import BetaSignupForm
from .models import Beta


class SignUp(generic.edit.CreateView):
    """
    This view handles users getting the ability to
    sign up to beta test the system
    """
    model = Beta
    form_class = BetaSignupForm
    template_name = 'beta/signup-form.html'
    success_url = reverse_lazy('beta-thanks')


class Thanks(generic.TemplateView):
    """
    Display a generic thank you message after successfully
    submitting :class:`SignUp`
    """
    template_name = 'beta/thanks.html'
