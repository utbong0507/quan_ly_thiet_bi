# Generated by Django 4.2.8 on 2023-12-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
