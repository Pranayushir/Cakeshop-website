# Generated by Django 4.2.5 on 2023-10-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_delete_shoppingcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default='No message provided'),
        ),
    ]
