# Generated by Django 4.2.13 on 2024-08-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
