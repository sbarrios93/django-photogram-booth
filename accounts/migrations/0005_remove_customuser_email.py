# Generated by Django 4.1.3 on 2022-12-03 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_customuser_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="email",
        ),
    ]