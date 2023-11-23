# Generated by Django 3.2.23 on 2023-11-23 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swimlane', '0003_coupon_is_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponcorporate',
            name='coupon_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='corporate_coupon', serialize=False, to='swimlane.coupon'),
        ),
        migrations.AlterField(
            model_name='couponindividual',
            name='coupon_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='individual_coupon', serialize=False, to='swimlane.coupon'),
        ),
    ]