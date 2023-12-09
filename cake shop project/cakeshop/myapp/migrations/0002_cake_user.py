# Generated by Django 4.2.5 on 2023-10-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cake',
            fields=[
                ('cakeid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='cakeimg')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
