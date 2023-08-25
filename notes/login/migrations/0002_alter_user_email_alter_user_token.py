# Generated by Django 4.2.4 on 2023-08-25 17:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
