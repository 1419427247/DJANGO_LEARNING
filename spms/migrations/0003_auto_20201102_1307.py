# Generated by Django 3.1.2 on 2020-11-02 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spms', '0002_auto_20201102_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='id',
            field=models.AutoField(default=1, editable=False, primary_key=True, serialize=False),
        ),
    ]
