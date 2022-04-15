from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.contrib import messages


class ContactUsView(FormView):
    template_name = "contact/contact_us.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form: ContactForm) -> HttpResponse:
        form.send_email()
        messages.add_message(request=self.request, message="Contact Form Submitted.", level=messages.SUCCESS)
        return super().form_valid(form)
