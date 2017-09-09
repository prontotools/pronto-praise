from django.conf.urls import url

from .views import (
    PraiseListView,
    PraiseAddView,
    PraiseAddHeart
)


urlpatterns = [
    url(r'^$', PraiseListView.as_view(), name='praise_list'),
    url(r'^add/$', PraiseAddView.as_view(), name='praise_add'),
    url(
        r'^(?P<praise_id>\d+)/heart/$', 
        PraiseAddHeart.as_view(), 
        name='praise_add_heart'
    ),
]
