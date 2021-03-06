# Generated by Django 3.2.2 on 2021-05-22 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlogApp', '0003_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='coverImage',
            field=models.ImageField(default='blogdefault.jpg', upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 14, 5, 45, 614992)),
        ),
    ]
