# Generated by Django 2.2.5 on 2019-09-27 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queryset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome')),
                ('desc', models.TextField(blank=True, max_length=255, null=True, verbose_name='Descrição')),
                ('distinct', models.BooleanField(default=False, help_text='\n        Útil quando relatórios que acessam muitas tabelas tem a possibilidade\n        de retornar resultados repetidos, marcar este campo desabilita a\n        repetição.', verbose_name='Distinguir')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificação')),
                ('automatic_generation', models.BooleanField(default=False, verbose_name='Geração Automática')),
                ('last_automatic_generation_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Última geração automática')),
                ('last_automatic_generation_xlsx', models.CharField(blank=True, editable=False, max_length=250, null=True, verbose_name='Último relatório gerado em XLSX')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Modelo')),
            ],
            options={
                'verbose_name': 'Modelo de Relatório',
                'verbose_name_plural': 'Modelos de Relatórios',
            },
        ),
        migrations.CreateModel(
            name='QueryFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=255, null=True, verbose_name='Código do Campo')),
                ('field_verbose', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do Campo')),
                ('field_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tipo do Campo')),
                ('lookup', models.CharField(choices=[('exact', 'Termo exato'), ('iexact', 'Termo exato (case-insensitivo)'), ('contains', 'Contém o termo'), ('icontains', 'Contém o termo (case-insensitivo)'), ('in', 'Termo está na lista'), ('gt', 'Maior que'), ('gte', 'Maior ou igual que'), ('lt', 'Menor que'), ('lte', 'Menor ou igual que'), ('startswith', 'Começa com'), ('istartswith', 'Começa com (case-insensitivo)'), ('endswith', 'Termina com'), ('iendswith', 'Termina com (case-insensitivo)'), ('range', 'Faixa/período'), ('year', 'Ano específico'), ('month', 'Mês específico'), ('day', 'Dia específico.'), ('isnull', 'É nulo?'), ('search', 'Busca textual'), ('regex', 'Expressão regular'), ('iregex', 'Expressão regular (case-insensitivo)')], max_length=11, verbose_name='Tipo de filtro')),
                ('method', models.CharField(choices=[('filter', 'Filtro'), ('exclude', 'Exclusão')], editable=False, max_length=7, verbose_name='Método')),
                ('readonly', models.BooleanField(default=False)),
                ('value_0', models.CharField(blank=True, max_length=255, null=True, verbose_name='Valor padrão 1')),
                ('value_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Valor padrão 2')),
                ('queryset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryset_reporter.Queryset')),
            ],
            options={
                'verbose_name': 'Filtros de query`s',
            },
        ),
        migrations.CreateModel(
            name='DisplayField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=255, null=True, verbose_name='Código do Campo')),
                ('field_verbose', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do Campo')),
                ('field_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tipo do Campo')),
                ('sort', models.CharField(blank=True, choices=[('asc', 'Crescente'), ('desc', 'Decrescente')], default=None, max_length=4, null=True, verbose_name='Ordenação')),
                ('annotate', models.CharField(blank=True, choices=[('Count', 'Somatório'), ('Ave', 'Média'), ('Max', 'Máximo'), ('Min', 'Mínimo')], max_length=5, null=True, verbose_name='Anotação')),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('pre_concatenate', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pré concatenação')),
                ('pos_concatenate', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pós concatenação')),
                ('queryset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryset_reporter.Queryset')),
            ],
            options={
                'verbose_name': 'Campo a exibir',
                'verbose_name_plural': 'Campos à exibir',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Exclude',
            fields=[
            ],
            options={
                'verbose_name': 'Exclusão',
                'verbose_name_plural': 'Exclusões',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('queryset_reporter.queryfilter',),
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
            ],
            options={
                'verbose_name': 'Filtro',
                'verbose_name_plural': 'Filtros',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('queryset_reporter.queryfilter',),
        ),
    ]
