# Generated by Django 3.2 on 2021-04-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_scheduling_scheduling_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='scheduling_done',
            field=models.CharField(blank=True, choices=[('1', 'Done'), ('2', 'Will be done'), ('3', 'Today')], max_length=1),
        ),
    ]
