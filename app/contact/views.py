from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin


class ContactUsView(SuccessMessageMixin, FormView):
    template_name = "contact/contact_us.html"
    form_class = ContactForm
    success_message = "Contact Form Submitted."
    success_url = "/"

    def form_valid(self, form: ContactForm) -> HttpResponse:
        form.send_email()
        return super().form_valid(form)
