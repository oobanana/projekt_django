# Generated by Django 2.0.5 on 2018-06-03 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180603_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tresc',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
