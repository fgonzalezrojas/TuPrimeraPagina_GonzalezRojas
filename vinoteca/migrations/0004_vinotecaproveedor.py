# Generated by Django 5.2 on 2025-04-15 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinoteca', '0003_rename_ean_vinotecaproducto_ean_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VinotecaProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=200)),
                ('cuit', models.IntegerField()),
                ('provincia', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=100)),
                ('codigo_postal', models.IntegerField()),
                ('calle', models.CharField(max_length=100)),
                ('altura', models.CharField(max_length=50)),
                ('iva', models.CharField(choices=[('RI', 'Responsable Inscripto'), ('MT', 'Monotributista'), ('CF', 'Consumidor fina')], max_length=100)),
                ('telefono', models.IntegerField()),
                ('mail', models.CharField(max_length=100)),
            ],
        ),
    ]
