# Generated by Django 3.2.23 on 2023-11-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimlane', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='is_valid',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]