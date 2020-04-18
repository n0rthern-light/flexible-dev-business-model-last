# Generated by Django 3.0.5 on 2020-04-18 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Template', max_length=50)),
                ('is_index_template', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('first_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('phone', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_private_section', models.BooleanField(default=True)),
                ('name', models.CharField(default='', max_length=75)),
                ('label', models.CharField(default='', max_length=250)),
                ('disclaimer', models.TextField(blank=True)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Template')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_field', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=75)),
                ('label', models.CharField(default='', max_length=250)),
                ('input_type', models.IntegerField(choices=[(1, 'Text'), (2, 'Number'), (3, 'Money'), (4, 'Email'), (5, 'Phone'), (6, 'Date'), (7, 'Check'), (8, 'Textarea'), (9, 'Select'), (10, 'List')], default=1)),
                ('default_value', models.TextField(blank=True, default='')),
                ('select_options', models.TextField(blank=True, default='')),
                ('template_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.TemplateSection')),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('state', models.IntegerField(choices=[(1, 'FORM_STATE_PENDING_ADMIN'), (2, 'FORM_STATE_PENDING_CLIENT'), (3, 'FORM_STATE_PENDING_INITIAL_PAYMENT'), (4, 'FORM_STATE_IN_PROGRESS'), (5, 'FORM_STATE_DONE')], default=1)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.User')),
                ('form_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Template')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='')),
                ('state', models.IntegerField(choices=[(1, 'FORM_RECORD_ACCEPTED_ONLY_CLIENT'), (2, 'FORM_RECORD_ACCEPTED_ONLY_ADMIN'), (3, 'FORM_RECORD_ACCEPTED_BOTH')])),
                ('init_user_side', models.IntegerField(choices=[(1, 'FORM_CLIENT'), (2, 'FORM_ADMIN')])),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('form_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Instance')),
            ],
        ),
    ]
