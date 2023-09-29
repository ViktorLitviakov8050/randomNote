# Generated by Django 4.2.5 on 2023-09-29 16:29

from django.db import migrations, models
import django.db.models.deletion
import randomNote.models


class Migration(migrations.Migration):

    dependencies = [
        ('randomNote', '0005_rename_isarchived_note_is_archived_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.TextField(unique=True),
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_checked', models.BooleanField(default=False)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='randomNote.note')),
            ],
            bases=(models.Model, randomNote.models.JSONSourceable),
        ),
    ]
