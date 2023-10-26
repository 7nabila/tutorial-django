
from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
=======
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')), #after
>>>>>>> 2463072c42a82cb8311a723d3ea446f3f14c761c
]

    #path("polls/", include("polls.urls")), #before