# Generated by Django 5.0.6 on 2024-05-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0008_alter_submission_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='c94e79830f434a1d8ef13e8c6a3cedc7', max_length=100, unique=True),
        ),
    ]
