# Generated by Django 4.1.7 on 2023-07-05 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_task_tasks_zerowaste'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks_zerowaste',
            old_name='zerowaste_user',
            new_name='zerowaste_user_id',
        ),
        migrations.AlterModelTable(
            name='tasks_zerowaste',
            table='tasks_zerowaste',
        ),
    ]