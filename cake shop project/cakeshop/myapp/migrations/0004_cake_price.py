# Generated by Django 4.2.5 on 2023-10-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='price',
            field=models.IntegerField(default=300),
        ),
    ]
