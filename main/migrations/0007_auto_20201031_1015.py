# Generated by Django 3.1.2 on 2020-10-31 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201031_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cookie',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
