from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, PostCategory


class PostCategorySitemap(Sitemap):
    # return that object’s change frequency as a string.
    changefreq = 'weekly'
    #return that object’s priority as either a string or float.
    priority = 0.9
    #A method that returns a sequence or QuerySet of objects. 
    def items(self):
        return PostCategory.objects.all()


class PostSitemap(Sitemap):
    # return that object’s change frequency as a string.
    changefreq = 'weekly'
    #return that object’s priority as either a string or float.
    priority = 0.9

    #A method that returns a sequence or QuerySet of objects. 
    def items(self):
        return Post.published.all()
    
    #an object as returned by items() – and return that object’s last-modified date/time as a datetime.
    def lastmod(self, obj):
        return obj.updated