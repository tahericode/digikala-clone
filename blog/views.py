from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, PostCategory
from django.core.paginator import Paginator
from .forms import CommentForm 
from django.db.models import Q
# Create your views here.

#Post list view
def post_list(request, category_slug=None):
    post_category = None
    # get all objects of post 
    posts =  Post.published.all()
    #show post by category__slug
    if category_slug:
        # get an object from category_slug 
        post_category = get_object_or_404(PostCategory, slug=category_slug)
        # filter post objects with category
        posts = posts.filter(category=post_category)
    # for search ---- 
    query = request.GET.get("q")
    # if query exists
    if query:
        # filter post objects with title or category__name using Q
        posts = posts.filter(Q(title__icontains=query) | Q(category__name__icontains=query)).distinct()   
    #last added post for show in Recent posts
    last_posts = posts[:8]
    # add Paginator
    paginator = Paginator(posts, 4) # number of show products in each page
    page_number = request.GET.get('page')
    pots_of_each_page = paginator.get_page(page_number) # page_obj = products in each page
    context = {
        'post_category': post_category,
        'posts': pots_of_each_page,
        'last_posts': last_posts,
    }
    return render(request, 'blog/post/list.html', context)

#Product Detail view
def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    #query for login user to show user characteristics
    if not request.user.is_anonymous:
        user = User.objects.get(username=request.user.username)
    #list of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        # validation
        if comment_form.is_valid():
            #Create Comment object but don,t save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.user = user
            #Save the comment to the datebase
            new_comment.save()
    else:
        comment_form = CommentForm()
    #Context for render page
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form, 
    }
    return render(request, 'blog/post/detail.html', context)