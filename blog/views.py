
# Create your views here.
from django.shortcuts import render
from .models import Post  # импорт модели Post

# Представление для отображения всех постов блога
def post_list(request):
    # Получаем все записи из базы данных, отсортированные по дате создания (от новых к старым)
    posts = Post.objects.all().order_by('-created_at')
    
    # Передаём записи в шаблон для отображения
    return render(request, 'blog/post_list.html', {'posts': posts})
