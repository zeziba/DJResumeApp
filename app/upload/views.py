import re
from typing import Any, Dict, Optional, Type
from django.http import HttpRequest, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView, FormView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ImagesForm
from .models import Images


# @staff_member_required
class ImageUploadView(SuccessMessageMixin, FormView):
    template_name = "upload/partials/upload.html"
    form_class = ImagesForm
    success_message = "Image Submited."
    success_url = "../images/"

    def get_form(self, form_class: Optional[Type[ImagesForm]] = ImagesForm) -> ImagesForm:
        return super(ImageUploadView, self).get_form(form_class)

    def form_valid(self, form: ImagesForm) -> HttpResponse:
        form.instance.save()
        self.success_message = f"Image Submited: {form.instance.image.url}"
        return super(ImageUploadView, self).form_valid(form)


# @staff_member_required
class ImagesView(TemplateView):
    template_name = "upload/images_display.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.all()
        return context
