# Generated by Django 4.2 on 2023-05-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleapp', '0005_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'completed'), ('IN PROGRESS', 'In progress')], max_length=50, null=True),
        ),
    ]