import imp
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings

TESTING_ADMIN = "admin@example.com"


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
    
    def send_email(self):
        subject = "Website Inquiry"
        body = {
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'email': self.cleaned_data['email_address'],
            'message': self.cleaned_data['message'],
        }
        message = "\n".join(body.values())
        
        try:
            if settings.DEBUG:
                send_mail(subject=subject, message=message, from_email=TESTING_ADMIN, recipient_list=[TESTING_ADMIN,])
            else:
                send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.EMAIL_DEST,])
        except BadHeaderError:
            return HttpResponse('Invalid header found')
