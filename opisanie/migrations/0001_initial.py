# Generated by Django 4.0.3 on 2022-06-17 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas_name', models.CharField(max_length=3, verbose_name='Буква класса')),
                ('clas_num', models.ImageField(upload_to='', verbose_name='Номер класса')),
            ],
            options={
                'verbose_name': 'class',
                'verbose_name_plural': 'Clases',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flf', models.CharField(max_length=255, verbose_name='\xa0ФИО-директора')),
                ('image', models.ImageField(upload_to='media/images', verbose_name='Фото директора')),
                ('numb', models.IntegerField(verbose_name='Номер директора')),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directors',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flf', models.CharField(max_length=255, verbose_name='ФИО-ученика')),
                ('clan_num', models.CharField(max_length=255, verbose_name='Класс ученика')),
                ('parents', models.IntegerField(max_length=255, verbose_name='Номер родителей ученика')),
                ('location', models.CharField(max_length=255, verbose_name='Место проживания ученика')),
                ('image', models.ImageField(upload_to='media/images', verbose_name='Фото ученика')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Sudents',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flf', models.CharField(max_length=255, verbose_name='ФИО-учителя')),
                ('location', models.CharField(max_length=255)),
                ('num', models.IntegerField(verbose_name='Номер учителя')),
                ('image', models.ImageField(upload_to='media/images', verbose_name='Фото учителя')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Zauch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flf', models.CharField(max_length=255, verbose_name='ФИО-завуча')),
                ('image', models.ImageField(upload_to='media/images', verbose_name='Фото завуча')),
                ('numb', models.IntegerField(verbose_name='Номер завуча')),
            ],
            options={
                'verbose_name': 'Zauch',
                'verbose_name_plural': 'Zauches',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessons', models.CharField(max_length=255)),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opisanie.clas', verbose_name='Классы')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opisanie.director', verbose_name='Директор школы')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opisanie.students', verbose_name='Ученики школы')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opisanie.teacher', verbose_name='Учителя')),
                ('zauch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opisanie.zauch', verbose_name='Завауч')),
            ],
        ),
        migrations.AddField(
            model_name='clas',
            name='clas_teacer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opisanie.teacher', verbose_name='Учитель класса'),
        ),
    ]
