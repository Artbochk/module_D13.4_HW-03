from django.contrib import admin
from django.forms import ModelMultipleChoiceField
from .models import NewsArticle, Category


class NewsArticleAdmin(admin.ModelAdmin):

    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('name', 'news_data', 'news_text', 'author') # оставляем только имя и цену товара
    list_filter = ('news_data', 'author','postCategory') # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'news_text',) # тут всё очень похоже на фильтры из запросов в базу


# Register your models here.
admin.site.register(Category)
admin.site.register(NewsArticle, NewsArticleAdmin)

