# Generated by Django 2.0.6 on 2018-06-19 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180619_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogUser'),
        ),
    ]
