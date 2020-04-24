from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from api.views import PostList, CategoryList, CategoryDetails, CategoryPostList
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('posts/', PostList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetails.as_view()),
    path('categories/<int:pk>/posts/', CategoryPostList.as_view())
]
