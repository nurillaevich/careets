from django.urls import path
from .views import AboutList, TeamList, ServiceList, AuthorList, CategoryList, TagList, BlogList, CommentList

urlpatterns = [
    path('about/', AboutList.as_view(), name='about'),
    path('team/', TeamList.as_view(), name='team'),
    path('service/', ServiceList.as_view(), name='service'),
    path('author/', AuthorList.as_view(), name='author'),
    path('category/', CategoryList.as_view(), name='category'),
    path('tag/', TagList.as_view(), name='tag'),
    path('blog/', BlogList.as_view(), name='blog'),
    path('comment/', CommentList.as_view(), name='comment'),
]

