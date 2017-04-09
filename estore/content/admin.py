from django.contrib import admin
from estore.content.models import Book, Television, Laptop, Mobile, Camera

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'section', 'authors', 'subject', 'publisher', 'publication_date', 'price', 'rating', 'description')
    list_filter = ('publication_date', 'section')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'photo', 'section', 'authors', 'subject', 'publisher', 'publication_date', 'price', 'rating', 'description')
    search_fields = ('title',)

class TVAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'tv_type', 'company', 'size', 'resolution', 'power', 'price','launch_date', 'rating', 'description')
    list_filter = ('company', 'tv_type')
    date_hierarchy = 'launch_date'
    ordering = ('-launch_date',)
    fields = ('title', 'photo', 'tv_type', 'company', 'size', 'resolution', 'power', 'price','launch_date', 'rating', 'description')
    search_fields = ('title',)

class LapAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'screen_size', 'company', 'resolution', 'power', 'processor', 'price', 'memory','graphics_card','accessories','launch_date', 'rating', 'description')
    list_filter = ('company', 'processor','memory')
    date_hierarchy = 'launch_date'
    ordering = ('-launch_date',)
    fields = ('title', 'photo', 'screen_size', 'company', 'resolution', 'power', 'processor', 'price', 'memory','graphics_card','accessories','launch_date', 'rating', 'description')
    search_fields = ('title',)


class MobAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'phone_type', 'company', 'camera', 'bluetooth', 'GPRS','size', 'price', 'weight','display_size', 'display_colours', 'battery', 'standby_time','accessories','launch_date', 'rating', 'description')
    list_filter = ('company', 'phone_type')
    date_hierarchy = 'launch_date'
    ordering = ('-launch_date',)
    fields = ('title', 'photo', 'phone_type', 'company', 'camera', 'bluetooth', 'GPRS','size', 'price', 'weight','display_size', 'display_colours', 'battery', 'standby_time','accessories','launch_date', 'rating', 'description')
    search_fields = ('title',)

class CamAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'company', 'model', 'optical_zoom', 'battery','digital_camera_type', 'price', 'memory_card_format','display_size', 'accessories','launch_date', 'rating', 'description')
    list_filter = ('company', 'model','digital_camera_type')
    date_hierarchy = 'launch_date'
    ordering = ('-launch_date',)
    fields = ('title', 'photo', 'company', 'model', 'optical_zoom', 'battery','digital_camera_type', 'price', 'memory_card_format','display_size', 'accessories','launch_date', 'rating', 'description')
    search_fields = ('title',)


admin.site.register(Book, BookAdmin)
admin.site.register(Television, TVAdmin)
admin.site.register(Laptop, LapAdmin)
admin.site.register(Mobile, MobAdmin)
admin.site.register(Camera, CamAdmin)



