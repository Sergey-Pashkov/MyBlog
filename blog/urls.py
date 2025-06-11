from django.urls import path
from . import views  # импортируем представления

urlpatterns = [
    # Путь к главной странице блога
    path('', views.post_list, name='post_list'),
]
