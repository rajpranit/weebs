# Generated by Django 4.0.4 on 2022-05-31 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weebs', '0012_remove_doujinspost_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doujins',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hentai',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manhua',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manhwa',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='watching',
            field=models.ManyToManyField(to='weebs.manhwa'),
        ),
    ]
