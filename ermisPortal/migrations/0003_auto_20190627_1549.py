# Generated by Django 2.1 on 2019-06-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ermisPortal', '0002_auto_20190625_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gn_is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='gn_is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='gn_is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='kb_is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='kb_is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
