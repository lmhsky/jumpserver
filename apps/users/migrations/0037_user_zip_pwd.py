# Generated by Django 3.1.13 on 2021-12-02 07:52

import common.fields.model
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_user_feishu_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zip_pwd',
            field=common.fields.model.EncryptCharField(blank=True, max_length=256, null=True, verbose_name='Zip password'),
        ),
    ]
