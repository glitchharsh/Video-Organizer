from django.urls import path
from django.views.generic import TemplateView
from .views import ListVideosAPI, ListSearchResultsAPI

urlpatterns = [
    path('list/', ListVideosAPI.as_view(), name='list_videos'),
    path('search/', TemplateView.as_view(template_name='search.html'), name='search_page'),
    path('', ListSearchResultsAPI.as_view(), name='search_result')
]