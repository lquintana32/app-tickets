# Generated by Django 4.0.5 on 2022-06-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_delete_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='solution',
            field=models.TextField(default=''),
        ),
    ]