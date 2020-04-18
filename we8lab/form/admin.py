from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import *


class TemplateQuestionInline(NestedStackedInline):
    model = TemplateQuestion
    extra = 1
    fk_name = 'template_section'


class TemplateSectionInline(NestedStackedInline):
    model = TemplateSection
    extra = 1
    fk_name = 'template'
    inlines = [TemplateQuestionInline]


class TemplateAdmin(NestedModelAdmin):
    inlines = [TemplateSectionInline]

    class Media:
        js = ('form/admin/js/base.js'),
        css = {"all": ('form/admin/base.css',)}


admin.site.register(Template, TemplateAdmin)
admin.site.register(User)
admin.site.register(Instance)
admin.site.register(History)