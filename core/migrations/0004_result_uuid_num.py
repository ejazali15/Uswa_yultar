# Generated by Django 5.0.6 on 2024-05-19 07:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_result_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='uuid_num',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
