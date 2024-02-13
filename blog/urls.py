from django.urls import path
from . import views

from .feeds import LatestPostsFeed

urlpatterns = [
    path("", views.post_list, name="post_list"),
    #path("", views.PostListView.as_view(), name="post_list"),
    path(r'^tag/(?P<tag_slug>[-\w]/$', views.post_list, name='post_list_by_tag'),
    path(r"^(P?<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/"\
         r"(?P<post>[-\w]+)/$",
         views.post_detail,
         name="post_detail"),
    path('feed/', LatestPostsFeed(), name="post_feed"),
    ]
