"""
URL configuration for project0 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first.views import Viewlogin,Viewsignin,Viewstudent,Viewbook,Booklist,Bookdetails,Book_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', Viewlogin.as_view()),
    path('signin/', Viewsignin.as_view()),
    path('student/', Viewstudent.as_view()),
    path('book/', Viewbook.as_view()),
    path('book/all', Booklist.as_view(),name="book-al"),
    path("book/<int:pk>", Bookdetails.as_view(),name="book-det"),
    path("book/<int:pk>/remove", Book_delete.as_view(),name="book-del"),
]
