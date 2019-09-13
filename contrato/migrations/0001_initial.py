# Generated by Django 2.1 on 2019-09-13 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContratActions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocknumber', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.BooleanField(null=True)),
                ('contract_address', models.CharField(blank=True, max_length=100, null=True)),
                ('from_adress', models.CharField(blank=True, max_length=100, null=True)),
                ('to_adress', models.CharField(blank=True, max_length=100, null=True)),
                ('transactionHash', models.CharField(blank=True, max_length=100, null=True)),
                ('gasUsed', models.CharField(blank=True, max_length=30, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criando em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('hash_address', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('abi', models.TextField(max_length=2000, null=True)),
                ('contract_address', models.CharField(blank=True, max_length=100, null=True)),
                ('solidity_version', models.CharField(blank=True, default='>=0.4.25 <0.6.0', max_length=20, null=True)),
                ('ativo', models.BooleanField(blank=True, null=True)),
                ('tipo', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criando em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('id_carteira', models.IntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente', verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ContratToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=15, null=True)),
                ('simbolo', models.CharField(blank=True, max_length=5, null=True)),
                ('quantidade', models.CharField(blank=True, max_length=5, null=True)),
                ('digitos', models.CharField(blank=True, max_length=5, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criando em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('id_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contrato.Contrato')),
            ],
        ),
        migrations.AddField(
            model_name='contratactions',
            name='id_contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contrato.Contrato'),
        ),
    ]