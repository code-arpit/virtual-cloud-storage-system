# Generated by Django 4.0.3 on 2022-04-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_plan', models.CharField(choices=[('Free plan', 'F'), ('Student Plam', 'S'), ('Organisation Plan', 'O')], default='Free plan', max_length=50)),
            ],
        ),
    ]