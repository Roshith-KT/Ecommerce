# Generated by Django 4.2.3 on 2023-08-02 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True, unique='True'),
        ),
    ]
