# Generated by Django 3.0.9 on 2020-08-11 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Creator'),
        ),
    ]
