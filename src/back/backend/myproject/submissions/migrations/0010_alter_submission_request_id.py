# Generated by Django 5.0.6 on 2024-05-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0009_alter_submission_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='9a8fe947d0e24caf8d5a62cc28414ffa', max_length=100, unique=True),
        ),
    ]
