# Generated by Django 2.2.7 on 2019-12-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_conferenceschedule_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferenceschedule',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]