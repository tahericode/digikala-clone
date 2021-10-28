from .models import PublicMassages

def publicMesseges(request):
    messages = PublicMassages.objects.filter(status='published')
    return({'messages':messages})