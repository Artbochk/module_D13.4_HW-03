from django.forms import ModelForm, ModelMultipleChoiceField, ModelChoiceField, MultipleChoiceField
from .models import NewsArticle, Category, PostCategory, Author


class NewsArticleForm(ModelForm):
    postCategory = ModelMultipleChoiceField(queryset=Category.objects.all(), label="Категория")



    class Meta:
        model = NewsArticle
        fields = ['name', 'news_text', 'postCategory']
