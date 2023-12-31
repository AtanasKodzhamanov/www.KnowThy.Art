# Generated by Django 4.1.7 on 2023-07-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0002_alter_artist_artist_painting_1_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artist",
            name="artist_painting_1",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="artist_painting_1_title",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="artist_painting_2",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="artist_painting_2_title",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="artist_painting_3",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="artist_painting_3_title",
        ),
        migrations.AlterField(
            model_name="artist",
            name="correct_answer",
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name="artist",
            name="incorrect_answer",
            field=models.IntegerField(default=5),
        ),
    ]
