# Generated by Django 3.1 on 2022-04-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line1',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_line2',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]