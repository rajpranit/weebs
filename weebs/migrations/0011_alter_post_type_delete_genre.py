# Generated by Django 4.0.4 on 2022-05-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weebs', '0010_alter_anime_author_alter_doujins_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Type',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.DeleteModel(
            name='genre',
        ),
    ]