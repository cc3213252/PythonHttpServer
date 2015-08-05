from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HttpLinuxServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_user_info_list/', 'HttpLinuxServer.views.get_user_info_list', name="get_user_info_list"),
    url(r'^update_user_info_list/', 'HttpLinuxServer.views.update_user_info_list', name="update_user_info_list"),
    url(r'^add_user_info_list/', 'HttpLinuxServer.views.add_user_info_list', name="add_user_info_list"),
    url(r'^delete_user_info_list/', 'HttpLinuxServer.views.delete_user_info_list', name="delete_user_info_list"),
)
