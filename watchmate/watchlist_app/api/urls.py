from django.urls import path
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailAV,
                                     StreamPlatformAV, StreamPlatformDetailAV,
                                     ReviewList, ReviewDetail)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream_list'),
    # path('stream/<int:pk>/review/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    # path('review/', ReviewList.as_view(), name='review_list'),
    # path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
]