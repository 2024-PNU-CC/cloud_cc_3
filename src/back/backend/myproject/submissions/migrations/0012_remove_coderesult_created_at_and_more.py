# Generated by Django 5.0.6 on 2024-05-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0011_coderesult_alter_submission_request_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coderesult',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='37d59bd9e5194e89810d0c232401b6f4', max_length=100, unique=True),
        ),
    ]
