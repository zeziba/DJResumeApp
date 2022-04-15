from django.db import models

max_cahr_length = 15


class SubmitImage(models.Model):
    location = models.URLField()

    def __str__(self) -> str:
        return f"{(len(self.location) > max_cahr_length) * '...'}{self.location[-max_cahr_length:]}"
