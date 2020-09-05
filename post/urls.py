from django.urls import path
from post.views import PostViewSet, DetailViewSet

urlpatterns = [
        path('', PostViewSet.as_view({'get':'get', 'post':'create'})), 
        path('/<int:pk>', DetailViewSet.as_view({'get':'get', 'delete':'delete', 'put':'update'})),
]
