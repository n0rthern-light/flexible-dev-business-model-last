from django.db import models
from django import forms
from .enums import EnumFormInstanceState, EnumFormRecordState, EnumFormRecordInitUser, EnumInputTypes
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Template(models.Model):
    name = models.CharField(max_length=50, default='Template')
    is_index_template = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TemplateSection(models.Model):
    is_private_section = models.BooleanField(default=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default='')
    label = models.CharField(max_length=250, default='')
    disclaimer = models.TextField(blank=True)
    css_class = models.CharField(max_length=150, default='', blank=True)


class TemplateQuestion(models.Model):
    required_field = models.BooleanField(default=False)
    is_negotiable = models.BooleanField(default=False)
    template_section = models.ForeignKey(TemplateSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default='')
    label = models.CharField(max_length=250, default='')
    input_type = models.IntegerField(choices=EnumInputTypes.choices(), default=int(EnumInputTypes.Text))
    disclaimer = models.CharField(max_length=150, blank=True)
    select_options = models.TextField(default='', blank=True)

    def __str__(self):
        return self.label


class Instance(models.Model):
    form_template = models.ForeignKey(Template, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('date published')
    state = models.IntegerField(choices=EnumFormInstanceState.choices(), default=int(EnumFormInstanceState.FORM_STATE_PENDING_ADMIN))

    def __str__(self):
        return self.form_template.name


class History(models.Model):
    form_instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    state = models.IntegerField(choices=EnumFormRecordState.choices())
    init_user_side = models.IntegerField(choices=EnumFormRecordInitUser.choices())
    created_date = models.DateTimeField('date published')