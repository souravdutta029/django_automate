from django.contrib import admin
from .models import CompressImage
from django.utils.html import format_html

# Register your models here.
class CompressImageAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />'.format(obj.compressed_img.url))
    
    def org_img_size(self, obj):
        size_in_mb = obj.original_img.size/(1024 * 1024)
        if size_in_mb > 1:
            return format_html(f'{size_in_mb:.2f} MB')
        else:
            size_in_kb = obj.original_img.size/(1024)
            return format_html(f'{size_in_kb:.2f} KB')
    
    def comp_img_size(self, obj):
        size_in_mb = obj.compressed_img.size/(1024 * 1024)
        if size_in_mb > 1:
            return format_html(f'{size_in_mb:.2f} MB')
        else:
            size_in_kb = obj.compressed_img.size/(1024)
            return format_html(f'{size_in_kb:.2f} KB')
    
    list_display = ('user', 'thumbnail', 'org_img_size', 'comp_img_size', 'quality', 'compressed_at')

admin.site.register(CompressImage, CompressImageAdmin)