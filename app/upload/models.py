from django.db import models

MAX_CHAR_LENGTH = 15
UPLOAD_LOCATION = 'uploads/'


class Images(models.Model):
    image = models.ImageField(upload_to=UPLOAD_LOCATION)

    def __str__(self) -> str:
        if self.image and hasattr(self.image, 'url'):
            return f"{(len(self.image.url) > MAX_CHAR_LENGTH) * '...'}{self.image.url[-MAX_CHAR_LENGTH:]}"
        else:
            return "Empty"
