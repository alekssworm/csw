# Generated by Django 5.0 on 2024-02-18 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_assignment_all_tonns_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='all_tonns',
        ),
    ]
