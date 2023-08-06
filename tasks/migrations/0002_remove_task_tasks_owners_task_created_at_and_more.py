# Generated by Django 4.2.4 on 2023-08-06 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tasks_owners',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='task_owner',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
    ]
