# Generated by Django 5.0.4 on 2024-04-22 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='dscription',
            new_name='description',
        ),
    ]
