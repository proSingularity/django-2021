# Generated by Django 3.2.7 on 2021-10-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
