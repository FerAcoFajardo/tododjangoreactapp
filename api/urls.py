from django.urls import path
from . import views


urlpatterns = [
    path('', views.ApiOverview.as_view(), name='api-overview'),
    path('task-list/', views.TaskListView.as_view(), name='api-listview'),
    path('task-detail/task:<str:pk>/', views.TaskDetailView.as_view(), name='api-detailview'),
    path('task-create/', views.TaskCreateView.as_view(), name='api-createview'),
    path('task-update/task:<str:pk>/', views.TaskUpdateView.as_view(), name='api-updateview'),
    path('task-delete/task:<str:pk>/', views.TaskDeleteView.as_view(), name='api-deleteview'),
]


