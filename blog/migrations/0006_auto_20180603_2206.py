# Generated by Django 2.0.5 on 2018-06-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='obrazek',
            field=models.FileField(blank=True, upload_to='image'),
        ),
    ]