# Generated by Django 3.1.2 on 2020-10-31 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201031_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cookie',
            field=models.CharField(blank=True, default='', max_length=32, unique=True),
        ),
    ]
