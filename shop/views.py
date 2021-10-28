from blog import models
from shop.models import Category, Product
from django.shortcuts import redirect, render, get_object_or_404
from . models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage
from taggit.models import Tag
from django.db.models import Count
from .forms import CommentForm
from django.db.models import Q
from django.contrib.auth.models import User
from .recommender import Recommender

# def for products
def product_list(request, category_slug=None, tag_slug=None):
    category = None
    # All categories
    categories = Category.objects.all()
    # All active products
    products = Product.objects.filter(available = True)
    # latest products
    latest_products = Product.objects.filter(available = True).order_by('-created')



    tag = None
    if tag_slug:
        # get object from Tag class with desired slug
        tag = get_object_or_404(Tag, slug=tag_slug)
        # get objects that filter by tags & available 
        products = Product.objects.filter(available='True',
                                        tags__in=[tag])

    if category_slug:
        # get objects from Category class that filter by slug
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)
        #show post by category__slug
    query = request.GET.get("q")
    if query:
        products = products.filter(Q(name__icontains=query) | Q(category__name__icontains=query)).distinct()

    #last added product for show in Recent posts
    last_posts = products[:8]
    # add Paginator
    paginator = Paginator(products, 4) # number of show products in each page
    page_number = request.GET.get('page')
    pots_of_each_page = paginator.get_page(page_number) # page_obj = products in each page




    context = {
        'category':category,
        'categories':categories,
        'products':pots_of_each_page,
        'latest_products':latest_products,
        'tag':tag,
        'last_posts':last_posts,
    }
    return render(request,'shop/list.html',context)



def product_detail(request, id, slug):
    # get product
    product = get_object_or_404(Product, id=id, slug=slug, available = True)
    if not request.user.is_anonymous:
        user = User.objects.get(username=request.user.username)
    # for recommendation
    products = Product.objects.filter(category = product.category)
    # for favorite
    fav = bool
    # if this product is favorite
    if product.favorite.filter(id = request.user.id).exists():
        fav = True
    # create an object from CartAddProductForm class 
    cart_product_form = CartAddProductForm()
    # recommender
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

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
            new_comment.user = user
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
        # 'similar_posts': similar_products,
        'recommended_products': recommended_products,
        'products':products,
        # favorite 
        'fav':fav,
        
    }
    return render(request, 'shop/detail.html', context)


