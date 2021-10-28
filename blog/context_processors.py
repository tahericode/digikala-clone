
from .models import PostCategory, Post

# context_processors for last posts & psot categories of blog
def blogSidebarInfo(request):
    posts = Post.published.all()
    last_posts = posts.order_by('-created')
    post_categories = PostCategory.objects.all()
    return({'last_posts':last_posts,'post_categories':post_categories })