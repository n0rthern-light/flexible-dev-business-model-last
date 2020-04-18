from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *


# Create your views here.
def index(request):
    index_tmp = Template.objects.filter(is_index_template=True).last()
    return HttpResponseRedirect(f'new/{index_tmp.id}/')


def new(request, id):
    new_form_template = Template.objects.filter(id=id).last()
    sections = TemplateSection.objects.filter(template=id)

    sections_and_questions = []
    for section in sections:
        section_questions = TemplateQuestion.objects.filter(template_section=section.id)
        sections_and_questions.append({
            'section_object': section,
            'section_questions': section_questions
        })

    template = loader.get_template('new/index.html')
    context = {
        'form_template': new_form_template,
        'sections_and_questions': sections_and_questions
    }
    return HttpResponse(template.render(context, request))


def view_form_by_id(request, id):
    return HttpResponse('You are viewing form ID: ' + id)