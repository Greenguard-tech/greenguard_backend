# Generated by Django 4.2.4 on 2024-12-07 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nursery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='users.user'),
        ),
    ]
