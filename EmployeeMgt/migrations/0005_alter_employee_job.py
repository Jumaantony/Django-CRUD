# Generated by Django 3.2.5 on 2021-07-29 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeMgt', '0004_auto_20210727_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeMgt.job'),
        ),
    ]
