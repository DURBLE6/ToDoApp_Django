# Generated by Django 4.2 on 2023-05-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleapp', '0004_remove_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'completed')], max_length=50, null=True),
        ),
    ]