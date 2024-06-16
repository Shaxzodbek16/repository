# Generated by Django 5.0.6 on 2024-06-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0006_alter_wish_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='game',
            field=models.ManyToManyField(to='repository.game'),
        ),
    ]
