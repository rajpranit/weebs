# Generated by Django 4.0.4 on 2022-05-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weebs', '0007_manhwa_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manhwa',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]