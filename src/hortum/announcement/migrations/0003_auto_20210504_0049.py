# Generated by Django 3.1.7 on 2021-05-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_announcement_idproductor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='type_of_product',
            field=models.CharField(choices=[('Artesanato', 'Artesanato'), ('Açúcar', 'Açúcar'), ('Bebidas', 'Bebidas'), ('Café', 'Café'), ('Carnes', 'Carnes'), ('Cogumelos', 'Cogumelos'), ('Derivados de trigo', 'Derivados de trigo'), ('Derivados de mandioca', 'Derivados de mandioca'), ('Derivados de cana', 'Derivados de cana'), ('Desidatrados', 'Desidratados'), ('Doces', 'Doces'), ('Flores', 'Flores'), ('Frango Caipira', 'Frango Caipira'), ('Frutas', 'Frutas'), ('Graos', 'Graos'), ('Hortaliças', 'Hortaliças'), ('Laticinios', 'Laticinios'), ('Legumes', 'Legumes'), ('Ovos de Galinha', 'Ovos de Galinha'), ('Peixes', 'Peixes'), ('Polpa de frutas', 'Polpa de frutas'), ('Pratos congelados', 'Pratos congelados'), ('Sorvetes', 'Sorvetes'), ('Outros', 'Outros')], default='Outros', max_length=200),
        ),
    ]
