# Generated by Django 4.2.5 on 2023-09-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_remove_note_bg_color_note_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_txt',
            field=models.TextField(),
        ),
    ]
