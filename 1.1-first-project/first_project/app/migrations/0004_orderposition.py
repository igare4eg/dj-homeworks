# Generated by Django 4.1.7 on 2023-05-15 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='app.product')),
            ],
        ),
    ]