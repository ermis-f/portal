# Generated by Django 2.1 on 2019-06-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ermisPortal', '0003_auto_20190627_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kb_is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
