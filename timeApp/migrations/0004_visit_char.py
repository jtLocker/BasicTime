# Generated by Django 2.2.5 on 2019-10-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeApp', '0003_visit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='char',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
