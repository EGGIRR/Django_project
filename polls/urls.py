from django.urls import path
from .views import BBLoginView, aplication_render
from . import views
from django.contrib.auth import views as authViews

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/', aplication_render, name='profile'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
