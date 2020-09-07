from post.views import PostViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
urlpatterns = router.urls

