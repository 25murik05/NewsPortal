from django.urls import path
from .views import NewsList, DetailNew

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', DetailNew.as_view())
]