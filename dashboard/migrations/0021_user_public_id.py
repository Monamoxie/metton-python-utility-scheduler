# Generated by Django 4.2.4 on 2023-12-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_alter_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public_id',
            field=models.CharField(blank=True, max_length=190, unique=True, verbose_name='public_id'),
        ),
    ]
