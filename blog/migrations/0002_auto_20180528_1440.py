# Generated by Django 2.0.5 on 2018-05-28 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odpowiedz_komentarz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='komentarz',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='komentarz',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Uzytkownik',
        ),
        migrations.AddField(
            model_name='odpowiedz_komentarz',
            name='komentarz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Komentarz'),
        ),
        migrations.AddField(
            model_name='odpowiedz_komentarz',
            name='odpowiedz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='odpowiedz', to='blog.Komentarz'),
        ),
    ]
