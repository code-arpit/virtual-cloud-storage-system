# Generated by Django 4.0.3 on 2022-04-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_alter_subscription_storage_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='storage_used',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]