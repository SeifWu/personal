# Generated by Django 3.1.7 on 2021-02-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seen', '0006_auto_20210224_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchedobject',
            name='cover',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]