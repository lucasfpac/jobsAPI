# Generated by Django 4.0.6 on 2024-04-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_jobpost_title_alter_jobpost_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='amount',
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='title',
            field=models.CharField(choices=[('installation', 'Instação'), ('support', 'Suporte'), ('additional', 'Adicional')], max_length=100),
        ),
    ]