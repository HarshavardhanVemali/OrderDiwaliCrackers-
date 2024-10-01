# Generated by Django 5.1.1 on 2024-10-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crakerapp', '0002_order_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedLoginAttempts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=255, unique=True)),
                ('attempts', models.PositiveBigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
