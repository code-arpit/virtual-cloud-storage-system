# Generated by Django 4.0.3 on 2022-04-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_subscription_storage_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='storage_used',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=4),
        ),
    ]
