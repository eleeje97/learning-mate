# Generated by Django 4.0.5 on 2022-06-21 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('qna_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qna_question', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('img_path', models.TextField(null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('quiz_question', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('quiz_answer', models.CharField(max_length=200)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailyclass.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QnA_answer',
            fields=[
                ('answer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qna_answer', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('qna_id', models.ForeignKey(db_column='qna_id', on_delete=django.db.models.deletion.CASCADE, to='dailyclass.qna')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file_url', models.FileField(upload_to='class_material/', verbose_name='uploaded_file')),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
