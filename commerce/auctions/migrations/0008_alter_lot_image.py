# Generated by Django 5.0.4 on 2024-04-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_lot_image_alter_lot_close_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='image',
            field=models.URLField(default=None, max_length=2000, verbose_name='Please insert link to image'),
        ),
    ]