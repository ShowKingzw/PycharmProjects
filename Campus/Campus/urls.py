from django.urls import path
from CampusServices import views 

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("index/", views.index, name ="index"),
    path("register/",views.register, name="register"),
    path("maps/", views.maps, name="maps"),
    path("lnglat/", views.lnglat, name="lnglat"),
    path("route/", views.route, name="route")
]
