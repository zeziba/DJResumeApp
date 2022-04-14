# Generated by Django 3.2.6 on 2022-04-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=120)),
                ('example', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='company_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
