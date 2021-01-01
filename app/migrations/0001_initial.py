# Generated by Django 3.1.4 on 2020-12-31 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Someone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('is_client', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SaleProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('quantity_type', models.CharField(choices=[('Kilogramo/s', 'Kilogramo/s'), ('Litro/s', 'Litro/s'), ('Unidad/es', 'Unidad/es'), ('Centimetros', 'Centimetros')], max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_type', models.CharField(max_length=25)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.sale')),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.someone'),
        ),
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('quantity_type', models.CharField(choices=[('Kilogramo/s', 'Kilogramo/s'), ('Litro/s', 'Litro/s'), ('Unidad/es', 'Unidad/es'), ('Centimetros', 'Centimetros')], max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.purchase')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.someone'),
        ),
    ]
