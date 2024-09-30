from django.urls import path,include
from . import views
urlpatterns = [
    # path("", views.home, name="home"),
    path("",views.homepage,name="homepage"),
    path("addEmployee/",views.add_employee,name="add_employee"),
    path("profile/<int:pk>",views.profile,name="employee_profile"),
    path("delete/<int:pk>/",views.delete_employee_info, name="delete_employee_info"),
    path("update/<int:pk>",views.update,name="update"),
    path("update_page/",views.update_page,name="update_page"),
    path("login/",views.login_view,name="login"),
    path('logout/',views.log_out,name="logout"),

]
