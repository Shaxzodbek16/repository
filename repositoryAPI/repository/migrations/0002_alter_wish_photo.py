# Generated by Django 5.0.6 on 2024-06-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='photo',
            field=models.BinaryField(),
        ),
    ]