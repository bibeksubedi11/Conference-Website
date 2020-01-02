# Generated by Django 2.2.7 on 2019-12-05 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferenceschedule',
            name='conference_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conference_day', to='website.ConferenceDay'),
        ),
    ]