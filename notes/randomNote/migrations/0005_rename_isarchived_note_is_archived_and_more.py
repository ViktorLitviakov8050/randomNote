# Generated by Django 4.2.4 on 2023-09-16 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomNote', '0004_alter_attachment_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='isArchived',
            new_name='is_archived',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='textContent',
            new_name='text_content',
        ),
    ]