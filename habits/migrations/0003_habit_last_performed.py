# Generated by Django 5.1.3 on 2024-11-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='last_performed',
            field=models.DateField(blank=True, null=True, verbose_name='Дата последнего выполнения'),
        ),
    ]
