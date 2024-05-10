from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailAV,
                                     StreamPlatformAV, StreamPlatformDetailAV,
                                     ReviewList, ReviewDetail, ReviewCreate,
                                     StreamPlatformViewSet)

router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch_detail'),
    
    path('', include(router.urls)),
    #path('stream/', StreamPlatformAV.as_view(), name='stream_list'),
    #path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    #path('review/', ReviewList.as_view(), name='review_list'),
    #path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    
]