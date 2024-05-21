from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="HomePage"),
    path("result/", views.result, name="result"),
    path("admissions/", views.admission, name="Admission"),
    path("blog/", views.blog, name="Blog"),
    path("blog/<str:pk>", views.blog_detail, name="Blog-detail"),
    path("login/", views.login_page, name="login_page_site"),
    path("sign-up/", views.sign_up, name="sign-up_page"),
    path("logout/", views.logout),
    path("result/<str:pk>", views.stud_result, name="Student_details"),
    path("certificate/", views.certificate, name="certificate_url"),
]
