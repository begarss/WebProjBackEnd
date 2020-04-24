from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from api.views import PostList, CategoryList, CategoryDetails, UserViewSet
from rest_framework_jwt.views import obtain_jwt_token

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('login/', obtain_jwt_token),
    # path('users/', UserViewSet.as_view()),
    path('posts/', PostList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetails.as_view()),
]
