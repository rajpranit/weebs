# Generated by Django 4.0.4 on 2022-06-02 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weebs', '0018_rename_poster_image_post_poster_image_lg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/Poster'),
        ),
    ]
