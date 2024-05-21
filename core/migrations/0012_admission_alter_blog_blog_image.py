# Generated by Django 5.0.6 on 2024-05-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_blog_blog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('student_cnic', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('student_field', models.CharField(default='lower than 9th class', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='blog_image/'),
        ),
    ]
