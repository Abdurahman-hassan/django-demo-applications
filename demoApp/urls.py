from django.urls import path, re_path

from . import views

# describe the app name to avoid confusion with other apps in the project
# that may have the same name for their views and urls files
app_name = 'demoApp'
handler404 = 'demoApp.views.handler404'

urlpatterns = [
    path('', views.index, name='index'),
    path('display_date/', views.display_date, name='display_date'),
    path('testmethods/', views.MyView.as_view(), name='testmethods'),
    # path('getuser/<str:name>/<int:id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path('showform/', views.showform, name="showform"),
    path('getform/', views.getform, name="redirect_get_form_data"),
    path('getdish/<str:dish_name>', views.custom_path_view, name='custompath'),
    path('permanent_redirect/', views.make_user_permanent_redirect, name='permanent_redirect'),

    # regex
    re_path(r'^getuser/(?P<name>[a-z]+)/(?P<id>[0-9]{1,2})/$', views.pathview, name='pathview'),
    re_path(r'^use_regex/getuser/([0-9]{1,2})/$', views.pathview2, name='pathview'),

]
