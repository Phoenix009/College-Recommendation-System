# Generated by Django 3.1.5 on 2021-10-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_auto_20211002_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='w0',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='w10',
            field=models.FloatField(blank=True, null=True),
        ),
    ]