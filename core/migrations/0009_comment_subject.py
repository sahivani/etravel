# Generated by Django 2.2.14 on 2020-10-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201015_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
