# Generated by Django 4.2.5 on 2023-09-14 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomNote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='created_at',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='updated_at',
            new_name='edited_time',
        ),
    ]
