
# Register your models here.
from django.contrib import admin
from .models import Post  # импортируем модель Post

# Регистрируем модель Post в административной панели
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Отображаемые столбцы в списке объектов
    list_display = ('title', 'created_at')

    # Поля, по которым можно искать
    search_fields = ('title',)

    # Поля только для чтения (например, чтобы нельзя было менять дату создания)
    readonly_fields = ('created_at',)
