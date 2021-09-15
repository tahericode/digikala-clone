from django.shortcuts import render
from shop.models import Product
from .forms import QuestionForm, ContactUsForm

def home_pageView(request):
    latest_products = Product.objects.filter(available = True).order_by('-created')
    most_popular_shops = Product.objects.filter(available = True).order_by('price')
    cheapest_shops = Product.objects.filter(available = True).order_by('-price')

    context = {
        'latest_products':latest_products,
        'most_popular_shops':most_popular_shops,
        'cheapest_shops':cheapest_shops
    }
    return render(request, 'details/statics/home.html', context)

def contact_us(requst):
    return render(requst, 'details/statics/contact_us.html', {})

def about_us(requst):
    return render(requst, 'details/statics/about.html', {})


def questions(request):
    if request.method == 'POST':
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            question_form.save()
            return render(request, 'details/statics/success.html', {})
        
    else:
        question_form = QuestionForm()

    return render(request, 'details/statics/questions.html',{'question_form': question_form})


def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return render(request, 'details/statics/success.html', {})
        
    else:
        contact_form = ContactUsForm()
    
    return render(request, 'details/statics/contact_us.html', {'contact_form': contact_form})
