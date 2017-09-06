from django.conf.urls import url

from .views import PraiseListView


urlpatterns = [
    url(r'^$', PraiseListView.as_view(), name='praise_list'),
]
