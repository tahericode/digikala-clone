from blog import models
from shop.models import Category, Product
from django.shortcuts import redirect, render, get_object_or_404
from . models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count
from .forms import CommentForm


def product_list(request, category_slug=None, tag_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    latest_products = Product.objects.filter(available = True).order_by('-created')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = Product.objects.filter(available='True',
                                        tags__in=[tag])

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)

    context = {
        'category':category,
        'categories':categories,
        'products':products,
        'latest_products':latest_products,
        'tag':tag,
    }
    return render(request,'shop/list.html',context)



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available = True)
    cart_product_form = CartAddProductForm()

    # List of similar posts
    product_tags_ids=product.tags.values_list('id', flat=True)
    similar_products = Product.objects.filter(available=True,
                                            tags__in=product_tags_ids,).exclude(id=product.id)
    similar_products = similar_products.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]



    # List of active comments for this post
    comments = product.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
            
    else:
        comment_form = CommentForm()



    context = {
        'product':product,
        'cart_product_form':cart_product_form,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'similar_posts': similar_products,

    }
    return render(request, 'shop/detail.html', context)
