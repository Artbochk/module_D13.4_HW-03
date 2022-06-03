from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
import django.forms
from .models import Category, NewsArticle, Author


class NewsArticleFilter(FilterSet):
    date = DateFilter(
        field_name='news_data',
        lookup_expr='exact',
        label="Дата",
        widget=django.forms.DateInput(attrs={'type': 'date'})
    )
    author = ModelChoiceFilter(
        queryset=Author.objects.all(),
        field_name='author',
        label="Автор",
    )

    postCategory = ModelChoiceFilter(
        queryset=Category.objects.all(),
        field_name='postCategory',
        label="Категория",
    )

    # class Meta:
    #     model = NewsArticle
    #     fields = ['postCategory']




