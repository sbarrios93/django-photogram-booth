# Generated by Django 4.1.3 on 2022-12-04 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_remove_followrequest_unique_requests_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followrequest",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipient",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="followrequest",
            name="sender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sender",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]