# Generated by Django 2.0.5 on 2019-05-10 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='文章标题', max_length=50)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('text', models.TextField(default='正文')),
            ],
        ),
    ]
