# Generated by Django 5.2 on 2025-04-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinoteca', '0002_rename_vinotecaproductos_vinotecaproducto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vinotecaproducto',
            old_name='ean',
            new_name='EAN',
        ),
        migrations.AddField(
            model_name='vinotecaproducto',
            name='etiqueta',
            field=models.CharField(default='Cheval Des Andes 1999', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vinotecaproducto',
            name='bebida',
            field=models.CharField(choices=[('Vino', 'Vino'), ('Whisky', 'Whisky'), ('Champagne', 'Champagne')], max_length=50),
        ),
    ]
