from django.contrib import admin
from articles.models import Article, Scope, ArticleScope


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleScopeInline
    ]


class ScopeAdmin(admin.ModelAdmin):
    inlines = [
        ArticleScopeInline
    ]


class ArticleScopeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Scope, ScopeAdmin)
admin.site.register(ArticleScope, ArticleScopeAdmin)
