from django.db import models

MAX_CHAR_LENGTH = 15
UPLOAD_LOCATION = f'uploads/'


class Images(models.Model):
    image = models.ImageField(upload_to=UPLOAD_LOCATION)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self) -> str:
        if self.image and hasattr(self.image, 'url'):
            return f"{(len(self.image.url) > MAX_CHAR_LENGTH) * '...'}{self.image.url[-MAX_CHAR_LENGTH:]}"
        else:
            return "Empty"
