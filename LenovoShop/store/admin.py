from django.contrib import admin
from .models import GoodsValue
from .models import ArticleCategory

# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = GoodsValue

admin.site.register(GoodsValue, GoodsAdmin)