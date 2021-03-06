# Generated by Django 3.0.7 on 2020-11-06 18:41

from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage
import rooms.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_datetime', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=1000)),
            ],
            options={
                'ordering': ['-posted_datetime'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('posted_datetime', models.DateTimeField(auto_now_add=True)),
                ('raw_file', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='files', validators=[rooms.validators.limit_file_size, rooms.validators.allowed_file_type], verbose_name='File')),
            ],
            options={
                'ordering': ['-posted_datetime'],
            },
        ),
        migrations.CreateModel(
            name='RoomBackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image_url', models.URLField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('slug', models.SlugField(default='', editable=False, max_length=100)),
                ('background', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.RoomBackground')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
