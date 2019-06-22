from django.urls import re_path
from . import views


urlpatterns = [

    re_path('^p/sql/$', views.page_p_sql, name='page_p_sql'),


]
