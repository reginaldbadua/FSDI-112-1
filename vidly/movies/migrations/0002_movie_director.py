# Generated by Django 2.1 on 2019-05-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]