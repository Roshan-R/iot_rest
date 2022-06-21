from django.urls import path
from .views import ReadingViews, MultipleView

urlpatterns = [
    path('', ReadingViews.as_view()),
    path('get/', MultipleView.as_view())
]
