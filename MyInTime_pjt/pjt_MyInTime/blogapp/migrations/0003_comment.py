# Generated by Django 3.1.5 on 2021-01-22 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20210123_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_user', models.TextField(max_length=20)),
                ('comment_thumbnail_url', models.TextField(max_length=300)),
                ('comment_textfield', models.TextField()),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogapp.blog')),
            ],
        ),
    ]
