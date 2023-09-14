from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostsList.as_view(), name='home'),
    path('create/', addpage, name='create'),
    path('post/<int:pk>/', PostOne.as_view()),
    path('post/resp/', addresp, name='addresp'),
    path('my/', RespSearch.as_view(), name='my'),
    path('my/resp/<int:pk>/delete/', RespDeleteView.as_view(), name='delete'),
    path('my/resp/send_message/', mail, name='send'),
]