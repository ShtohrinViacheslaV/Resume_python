from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
]
