from django.urls import path
from Test import views 

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("login/", views.login, name ="login"),
    path("register/",views.register, name="register")
]
