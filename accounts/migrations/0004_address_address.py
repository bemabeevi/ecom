# Generated by Django 4.2.1 on 2023-07-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_address_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
