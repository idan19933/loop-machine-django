# Generated by Django 4.0.4 on 2022-04-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sound', '0005_remove_sound_audio_file4_remove_sound_audio_file5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sound',
            name='audio_file4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sound',
            name='audio_file5',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sound',
            name='audio_file6',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sound',
            name='audio_file7',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sound',
            name='audio_file8',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sound',
            name='audio_file9',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
