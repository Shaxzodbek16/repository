# Generated by Django 5.0.6 on 2024-06-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0017_alter_person_birthday_alter_person_connected_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='connected_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='shaxzodbek',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wish',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
