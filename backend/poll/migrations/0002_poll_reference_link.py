# Generated by Django 4.2 on 2023-04-16 11:39

from django.db import migrations, models
import poll.models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='reference_link',
            field=models.CharField(default=poll.models.generate_reference_link, max_length=16, unique=True),
        ),
    ]