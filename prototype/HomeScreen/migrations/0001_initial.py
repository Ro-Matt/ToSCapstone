# Generated by Django 4.0.2 on 2022-02-18 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('explanation', models.CharField(max_length=500, null=True)),
                ('weight', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Ownership', 'Ownership'), ('Privacy/Data', 'Privacy/Data')], max_length=15)),
                ('valid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contributions', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fullText', models.TextField(blank=True)),
                ('weightRating', models.FloatField(blank=True)),
                ('communityRating', models.FloatField(blank=True)),
                ('annotations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HomeScreen.edit')),
            ],
        ),
        migrations.AddField(
            model_name='edit',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='HomeScreen.user'),
        ),
        migrations.AddField(
            model_name='edit',
            name='element',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='HomeScreen.element'),
        ),
    ]
