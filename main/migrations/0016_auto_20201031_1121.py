# Generated by Django 3.1.2 on 2020-10-31 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20201031_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cookie',
            field=models.CharField(editable=False, max_length=32, null=True, unique=True),
        ),
    ]