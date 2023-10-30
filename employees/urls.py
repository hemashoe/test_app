from django.contrib import admin
from django.urls import path
from orgchart.views import department_tree


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", department_tree, name="department_tree"),
]
