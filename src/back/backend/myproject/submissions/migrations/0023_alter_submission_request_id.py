# Generated by Django 5.0.6 on 2024-05-31 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0022_alter_submission_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='86e64e8780264601a89c32306aa70228', max_length=100, unique=True),
        ),
    ]
