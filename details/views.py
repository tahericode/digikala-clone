from django.shortcuts import render, redirect
from shop.models import Product
from .forms import QuestionForm, ContactUsForm
from django.utils.translation import activate

# def for home page 
def home_pageView(request):
    products = Product.objects.filter(available = True)
    latest_products = products.order_by('-created')
    most_popular_shops = products.filter(available = True).order_by('price')
    cheapest_shops = Product.objects.filter(available = True).order_by('-price')
    context = {
        'latest_products':latest_products,
        'most_popular_shops':most_popular_shops,
        'cheapest_shops':cheapest_shops,
    }
    return render(request, 'details/statics/home.html', context)



def change_lang(request):
    
    activate(request.GET.get('lang'))
    return redirect(request.GET.get('next'))


# def for contact_us
def contact_us(requst):
    return render(requst, 'details/statics/contact_us.html', {})

# def for about_us
def about_us(requst):
    return render(requst, 'details/statics/about.html', {})

# def for questions
def questions(request):
    if request.method == 'POST':
        # create object from QuestionForm
        question_form = QuestionForm(data=request.POST)
        # form validation
        if question_form.is_valid():
            #save the form
            question_form.save()
            return render(request, 'details/statics/success.html', {})
    else:
        # if request.method is not euqal POST
        question_form = QuestionForm()
    return render(request, 'details/statics/questions.html',{'question_form': question_form})

# def for contact_us
def contact_us(request):
    if request.method == 'POST':
        #create object from ContactusForm
        contact_form = ContactUsForm(data=request.POST)
        # form validation
        if contact_form.is_valid():
            #save the form
            contact_form.save()
            return render(request, 'details/statics/success.html', {})
    else:
        # if request.method is not euqal POST
        contact_form = ContactUsForm()
    return render(request, 'details/statics/contact_us.html', {'contact_form': contact_form})
