import os
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    def generate_super(apps, schema_editor):
        from django.contrib.auth.models import User

        DJ_SU_USER = os.environ.get("DJ_SU_USER")
        DJ_SU_EMAIL = os.environ.get("DJ_SU_EMAIL")
        DJ_SU_PW = os.environ.get("DJ_SU_PW")

        superuser = User.objects.create_superuser(
            username=DJ_SU_USER,
            email=DJ_SU_EMAIL,
            password=DJ_SU_PW
        )

        superuser.save()

    operations = [
        migrations.RunPython(generate_super),
    ]
