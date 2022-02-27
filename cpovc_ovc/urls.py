"""OVC care section urls."""
from django.urls import path
from cpovc_ovc.views import(ovc_home,ovc_search,ovc_register,ovc_edit,ovc_view,hh_manage)

# This should contain urls related to registry ONLy
urlpatterns = [
    path(r'^$', ovc_home, name='ovc_home'),
    path(r'^ovc/search/$', ovc_search, name='ovc_search'),
    path(r'^ovc/new/<int: id>/$',ovc_register, name='ovc_register'),
    path(r'^ovc/edit/<int: id>/$',ovc_edit, name='ovc_edit'),
    path(r'^ovc/view/<int: id>/$',ovc_view, name='ovc_view'),
    path(r'^hh/view/<int: id>/$',hh_manage, name='hh_manage')
]
