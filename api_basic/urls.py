from django.urls import path, include
from .views import ArticleAPIView, ArticleDetail, GenericAPIView, ArticleViewSet, ArticleViewSetoo
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article', ArticleViewSetoo, basename='article')
urlpatterns = [
    # path('article/', article_list),
    path('api/v1/article/', ArticleAPIView.as_view()),
    path('api/v1/article/<int:id>/', ArticleDetail.as_view()),

    path('api/v1/generic/article/', GenericAPIView.as_view()),
    path('api/v1/generic/article/<int:id>/', GenericAPIView.as_view()),

    path('api/v1/viewset/', include(router.urls)),
    path('api/v1/viewset/<int:pk>/', include(router.urls)),

    path('api/v1/viewsetmodel/', include(router.urls)),
    path('api/v1/viewsetmodel/<int:pk>/', include(router.urls)),

]
