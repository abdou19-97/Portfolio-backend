# Generated by Django 4.2.4 on 2023-09-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_firstname_alter_user_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(max_length=264),
        ),
    ]