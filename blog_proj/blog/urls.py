
from django.urls import path
from .views import PostView,post_detail,post_edit,post_delete


urlpatterns = [
    path("blog/", PostView, name = 'postview'),
    path("post_detail/<int:pk>/", post_detail,name ="postdetail"),
    path("post_edit/<int:pk>/", post_edit,name ="postedit"),
     path("post_delete/<int:pk>/", post_delete,name ="postdelete")
]
