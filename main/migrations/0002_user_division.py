# Generated by Django 4.2.7 on 2023-12-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='division',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
