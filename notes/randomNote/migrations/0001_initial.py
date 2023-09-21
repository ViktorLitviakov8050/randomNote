# Generated by Django 4.2.5 on 2023-09-14 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textContent', models.TextField()),
                ('title', models.TextField()),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('isArchived', models.BooleanField()),
                ('labels', models.ManyToManyField(to='randomNote.label')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.TextField()),
                ('mime_type', models.TextField()),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randomNote.note')),
            ],
        ),
    ]