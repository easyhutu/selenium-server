# Generated by Django 2.0 on 2017-12-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='task name')),
                ('status', models.CharField(choices=[('waiting', '等待中'), ('running', '执行中'), ('finished', '结束')], default='waiting', max_length=20, verbose_name='status')),
                ('task_env', models.CharField(choices=[('test', '测试服务器'), ('prod', '正式服务器')], default='test', max_length=20, verbose_name='task env')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('start_time', models.DateTimeField(auto_now=True, verbose_name='task stat time')),
                ('end_time', models.DateTimeField(auto_now=True, verbose_name='task end time')),
                ('task_report', models.TextField(verbose_name='task report')),
            ],
        ),
    ]
