from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path,include
from api.views import Favorites,PostList,CategoryList,PostListPublished, CategoryDetails, CategoryPostList, UserViewSet,VacancyList,post_details,published_list
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
    path('login/', obtain_jwt_token),
    path('admin/', PostList.as_view()),
    path('admin/<int:post_id>/', post_details),

    path('posts/', PostListPublished.as_view()),
    path('posts/<int:post_id>/', post_details),
    path('fav/', Favorites.as_view()),

    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetails.as_view()),
    path('categories/<int:pk>/posts/', CategoryPostList.as_view())

]
