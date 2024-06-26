# Generated by Django 5.0.6 on 2024-05-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0010_alter_submission_request_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=100)),
                ('result', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='a7d4f85d2c5f4f68832ed9d359694244', max_length=100, unique=True),
        ),
    ]
