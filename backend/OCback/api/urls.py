from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path,include
from api.views import PostList, CategoryList, CategoryDetails, CategoryPostList, UserViewSet
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
    path('login/', obtain_jwt_token),
    path('posts/', PostList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetails.as_view()),
    path('categories/<int:pk>/posts/', CategoryPostList.as_view())
]
