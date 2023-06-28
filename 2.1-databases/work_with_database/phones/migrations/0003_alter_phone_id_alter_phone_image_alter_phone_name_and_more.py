# Generated by Django 4.1.7 on 2023-05-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_id_alter_phone_image_alter_phone_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(upload_to='phones'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
