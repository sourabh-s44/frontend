# Generated by Django 4.2.3 on 2023-08-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_customerinfo_customerorder_materialtype_orderdetail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='name',
            field=models.CharField(default='TestSensor', max_length=100),
        ),
    ]
