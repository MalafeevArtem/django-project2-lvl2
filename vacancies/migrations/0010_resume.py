# Generated by Django 3.1.3 on 2020-12-09 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0009_auto_20201209_0822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('status', models.CharField(choices=[('looking_for_a_job', 'Ищу работу'), ('open_to_suggestions', 'Открыт к предложениям'), ('not_looking_for_a_job', 'Не ищу работу')], max_length=64)),
                ('salary', models.IntegerField()),
                ('grade', models.CharField(choices=[('junior', 'Младший (junior)'), ('middle', 'Средний (middle)'), ('senior', 'Страший (senior)')], max_length=64)),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('portfolio', models.TextField()),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.specialty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
