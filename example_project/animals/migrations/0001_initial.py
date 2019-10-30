from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phylum', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_name', models.CharField(max_length=255)),
                ('family_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Class')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genus_name', models.CharField(max_length=255)),
                ('scientific_name', models.CharField(max_length=255)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Family')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('race', models.CharField(blank=True, max_length=255)),
                ('sex', models.CharField(blank=True, choices=[('f', 'Female'), ('m', 'Male'), ('h', 'Hermaphrodite')], max_length=2)),
                ('photo', models.ImageField(blank=True, height_field='photo_height', upload_to='animals', width_field='photo_width')),
                ('photo_height', models.IntegerField(blank=True, editable=False, null=True)),
                ('photo_width', models.IntegerField(blank=True, editable=False, null=True)),
                ('owners', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Specie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
