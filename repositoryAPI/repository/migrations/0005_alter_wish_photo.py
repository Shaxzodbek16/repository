# Generated by Django 5.0.6 on 2024-06-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_alter_wish_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
