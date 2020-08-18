from django.urls import path, include
from event import views
from comment.views import comment_detail

app_name = 'event'

urlpatterns = [
    path('register/', views.register_event, name="event_register"),
    path('creator_event/<int:pk>/',views.creator_detail, name='creator_detail'),
    path('creator_event/<int:pk>/comment', comment_detail, name='comment_detail'),

    path('search_result/', views.search_result, name='search_result')
]