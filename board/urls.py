from django.contrib import admin
from django.urls import path, include
from post.views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='user')
urlpatterns = router.urls
# 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('post.urls')),
# ]

