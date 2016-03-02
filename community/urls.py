from django.conf.urls import url


from .views import (
    post_create,
    post_delete,
    post_detail,
    post_list,
    post_update,
    home,
)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^create/$', post_create),
    url(r'^list/$', post_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'), # detail view
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    # url(r'^posts/$', "community.views.post_home"),
    # url(r'^posts/$', "<app_name>.views.<function_name>"),

]
