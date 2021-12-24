# Generated by Django 3.2.9 on 2021-12-23 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_usermodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('comment_time', models.DateTimeField()),
                ('comment_content', models.TextField()),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.usermodel')),
            ],
        ),
    ]
