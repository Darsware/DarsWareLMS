# Generated by Django 5.0 on 2024-10-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_country_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(default='XX', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(related_name='books', to='books.country'),
        ),
    ]