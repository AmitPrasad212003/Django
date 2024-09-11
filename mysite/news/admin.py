from django.contrib import admin
from news.models import News

class NewsAdim(admin.ModelAdmin):
    list_display = ('news_title', 'news_desc','news_image')

admin.site.register(News,NewsAdim)
# Register your models here.
