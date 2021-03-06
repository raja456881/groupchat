from django.urls import path
from.import views

urlpatterns = [
   path("home/", views.index, name="login"),
   path("sigup/", views.register, name="sigin"),
   path("login/", views.handlelogin, name="login"),
    path("sighand", views.handlesignup, name="sigin1"),
    path("logout", views.handlelogout, name="logout"),
    path("", views.home, name="home"),
    path("userdetails", views.AllUserDetail, name="userdetails"),
    path("updateuser/<int:myid>", views.AuthorUpdateView.as_view()),
    path('chat/<str:username>/', views.room, name='room'),
    path("creategroup", views.creategroup, name="creategroup"),
    path("groupdetails/", views.Groupdetails.as_view()),
    path('chatgroup/<group1>', views.groupchat, name="group"),
    path('joint/', views.JoinGroup.as_view()),
    path('leave/', views.LeaveGroup.as_view())

    ]