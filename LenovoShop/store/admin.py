from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = GoodsValue

class ArticleCategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = ArticleCategory

admin.site.register(GoodsValue, GoodsAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
=======
>>>>>>> 9c1b8ca9d9f0daf26d65851759cecf0ef43fcd70
