# Generated by Django 4.1.2 on 2022-11-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dreamreal",
            name="email",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="dreamreal",
            name="pid",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]