# Generated by Django 3.2.7 on 2021-10-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_hostname_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostname',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
