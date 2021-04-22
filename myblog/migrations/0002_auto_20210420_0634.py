# Generated by Django 3.2 on 2021-04-19 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='halaman',
            name='waktu',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Buku',
        ),
        migrations.DeleteModel(
            name='Kelompok',
        ),
    ]
