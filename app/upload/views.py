import imp
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required

from .models import SubmitImage


@staff_member_required
def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        SubmitImage.objects.create(location=image_url)
        return render(request, "upload/partials/upload.html", {
            "image_url": image_url
        })
    return render(request, "upload/partials/upload.html")
