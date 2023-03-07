from django.urls import path
from View.views import ComicList, ComicDetail, PublisherList, PublisherDetail

urlpatterns = [
    path('comic/', ComicList.as_view()),
    path('comic/<int:pk>/', ComicDetail.as_view()),
    path('publisher/', PublisherList.as_view()),
    path('publisher/<int:pk>/', PublisherDetail.as_view()),
]