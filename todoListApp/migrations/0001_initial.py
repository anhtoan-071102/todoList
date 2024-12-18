# Generated by Django 5.1.4 on 2024-12-04 19:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.TextField(verbose_name=200)),
                ('describe', models.TextField(verbose_name=1000)),
                ('status', models.CharField(choices=[('PENDING', 'chưa thực hiện'), ('IN_PROGRESS', 'đang tiến hành'), ('COMPLETED', 'đã hoàn thành'), ('OVERDUE', 'quá hạn')], default='PENDING', max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
