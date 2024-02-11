from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse

from .models import *
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    # tao ra form cho phep tuong tac voi all fields cua model Lesson
    # trong do field content duoc de` len nhu tren
    class Meta:
        model = Lesson
        fields = '__all__'


# thiet lap inlines cho n-n
class LessonTagInlineAdmin(admin.TabularInline):
    model = Lesson.tags.through


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ["id", "subject", "create_date", "course", "active"]
    search_fields = ["subject", "create_date", "course__subject"]
    list_filter = ['subject', 'course__subject']
    readonly_fields = ['avatar']  # trung` ten thi` k dc
    inlines = [LessonTagInlineAdmin]

    def avatar(self, lesson):
        if lesson:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=lesson.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/main.css',)
        }


# inlineModelAdmin: nhung' form cua con vao` cha
# the hien cac lesson co trong course or tao lesson moi khi ma chinh sua course
class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    fk_name = 'course'


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin]


class TagAdmin(admin.ModelAdmin):
    inlines = [LessonTagInlineAdmin]


# them view vao trang admin
class CourseAppAdminSite(admin.AdminSite):
    site_header = 'He thong khoa hoc truc tuyen'

    def get_urls(self):
        return [path('course-stats/', self.course_stats)] + super().get_urls()

    def course_stats(self, request):
        count = Course.objects.filter(active=True).count()
        # lesson_count=Count('lessons')): lessons la lay tu related_name
        stats = Course.objects.annotate(lesson_count=Count('lessons')).values('id', 'subject', 'lesson_count')
        return TemplateResponse(request, 'admin/course-stats.html',
                                {'course_count': count,
                                 'course_stats': stats})


admin_site = CourseAppAdminSite(name='Myadmin')
# Register your models here.
admin_site.register(Category)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)
admin_site.register(Tag, TagAdmin)
