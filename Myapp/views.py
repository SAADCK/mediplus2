from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def doctor_list(request):
    return render(request, 'dr_list.html')

def contact(request):
    return render(request, 'contact.html')

def ai_bot(request):
    return render(request, 'AI BOT.html')
def appointment_view(request):
    return render(request, 'booking.html')
def blog_single(request):
    return render(request, 'blog-single.html')
def portfolio_details(request):
    return render(request, 'portfolio-details.html')