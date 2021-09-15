from django.shortcuts import render,get_object_or_404
from . import models
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Count



def post_list(request, category_slug=None, tag_slug=None):
    category = None
    tag = None
    categories = models.Category.objects.all()
    posts = models.Post.published.all()
    latest_posts = models.Post.objects.filter(status='published').order_by('-created')
    

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in = [tag])

    if category_slug:
        category = get_object_or_404(models.Category, slug = category_slug)
        posts = posts.filter(category = category)

    context = {
        'category':category,
        'categories':categories,
        'posts':posts,
        'latest_posts':latest_posts,
        'tag': tag,
    }
    
    return render(request,'blog/post/list.html', context)



def post_detail(request, year, month, day, post):
    post = get_object_or_404(models.Post,
                            slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
   
    # List of similar posts
    post_tag_ids = post.tags.values_list('id', flat=True)
    similar_posts = models.Post.published.filter(tags__in = post_tag_ids).exclude(id = post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post':post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'similar_posts': similar_posts,
       
    }
    return render(request, 'blog/post/detail.html', context)
        
