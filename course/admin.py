from django.contrib import admin
from django.utils.html import format_html
from .models import Course, Note


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview', 'title', 'description_short')
    search_fields = ('title', 'description')
    readonly_fields = ('thumbnail_preview',)

    fieldsets = (
        ('Course Info', {
            'fields': ('title', 'description')
        }),
        ('Media Upload', {
            'fields': ('thumbnail', 'video')
        }),
        ('Thumbnail Preview', {
            'fields': ('thumbnail_preview',)
        }),
    )

    def thumbnail_preview(self, obj):
        # obj.pk is None when adding a new course
        if obj.pk and obj.thumbnail:
            return format_html(
                '<img src="{}" style="width:200px; height:120px; object-fit:cover; border-radius:8px;">',
                obj.thumbnail.url
            )
        elif not obj.pk:
            return "Save the course first to see the preview."
        else:
            return "No thumbnail uploaded yet."
    thumbnail_preview.short_description = 'Current Thumbnail'

    def description_short(self, obj):
        return obj.description[:60] + '...' if len(obj.description) > 60 else obj.description
    description_short.short_description = 'Description'


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'description_short')
    list_filter = ('language',)
    search_fields = ('title', 'description')

    fieldsets = (
        ('Note Info', {
            'fields': ('title', 'description', 'language')
        }),
        ('File', {
            'fields': ('file',)
        }),
    )

    def description_short(self, obj):
        return obj.description[:60] + '...' if len(obj.description) > 60 else obj.description
    description_short.short_description = 'Description'


admin.site.site_header = "LearnWithLucky Admin"
admin.site.site_title = "LearnWithLucky"
admin.site.index_title = "Welcome to LearnWithLucky Admin Panel"