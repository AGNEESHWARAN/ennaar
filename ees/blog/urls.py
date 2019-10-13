from blog import views
from django.urls import path,include


app_name='blog'

urlpatterns=[
    path('',views.viweBlog,name='viewblog'),
    path('postblog/',views.postBlog,name='postblog'),
    path('delete/',views.deletepost,name='delete'),
    path('deleteblog/',views.deleteblog,name='deleteblog')
]
