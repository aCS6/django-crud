# Generated by Django 4.0.6 on 2022-07-10 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='name',
        ),
    ]
