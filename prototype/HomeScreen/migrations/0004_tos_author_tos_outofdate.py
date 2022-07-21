# Generated by Django 4.0.2 on 2022-04-13 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HomeScreen', '0003_profile_tos_category_tos_communityrating_tos_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tos',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tos',
            name='outOfDate',
            field=models.BooleanField(default=False),
        ),
    ]