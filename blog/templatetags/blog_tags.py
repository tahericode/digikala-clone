from django import template
from ..models import Post


register = template.Library()

@register.simple_tag
def show_latest_posts(count=6):
    latest_posts = Post.published.order_by('-publish')[:count]
    return latest_posts