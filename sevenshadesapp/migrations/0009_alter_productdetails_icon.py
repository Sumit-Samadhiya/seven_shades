# Generated by Django 5.0.2 on 2024-04-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevenshadesapp', '0008_alter_productdetails_offerprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='icon',
            field=models.TextField(default=''),
        ),
    ]