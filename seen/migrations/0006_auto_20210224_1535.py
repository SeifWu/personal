# Generated by Django 3.1.7 on 2021-02-24 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seen', '0005_watchedobject_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchedobject',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watched_objects', to=settings.AUTH_USER_MODEL),
        ),
    ]