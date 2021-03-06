# Generated by Django 4.0.2 on 2022-03-10 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeScreen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('associatedText', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.AlterModelOptions(
            name='element',
            options={'ordering': ['pk']},
        ),
        migrations.RemoveField(
            model_name='element',
            name='valid',
        ),
        migrations.RemoveField(
            model_name='tos',
            name='annotations',
        ),
        migrations.RemoveField(
            model_name='tos',
            name='communityRating',
        ),
        migrations.RemoveField(
            model_name='tos',
            name='weightRating',
        ),
        migrations.AddField(
            model_name='tos',
            name='elements',
            field=models.ManyToManyField(through='HomeScreen.ElementText', to='HomeScreen.Element'),
        ),
        migrations.AlterField(
            model_name='tos',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='elementtext',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeScreen.element'),
        ),
        migrations.AddField(
            model_name='elementtext',
            name='tos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeScreen.tos'),
        ),
        migrations.AlterUniqueTogether(
            name='elementtext',
            unique_together={('element', 'tos')},
        ),
    ]
