# Generated by Django 5.1.1 on 2024-09-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0002_alter_employee_info_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_info',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
