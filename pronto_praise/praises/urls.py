from django.conf.urls import url

from .views import (
    PraiseListView,
    PraiseAddView,
)


urlpatterns = [
    url(r'^$', PraiseListView.as_view(), name='praise_list'),
    url(r'^add/$', PraiseAddView.as_view(), name='praise_add'),
]
