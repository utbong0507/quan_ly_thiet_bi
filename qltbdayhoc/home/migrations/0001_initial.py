# Generated by Django 4.2.8 on 2023-12-10 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mon', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('hansudung', models.CharField(max_length=255)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muon', models.CharField(max_length=255)),
                ('tra', models.CharField(max_length=255)),
                ('lop', models.CharField(max_length=255)),
                ('giaovien', models.CharField(max_length=255)),
                ('tiet', models.CharField(max_length=255)),
                ('deviceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.device')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]