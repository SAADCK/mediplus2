from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Appointment, Doctor
from django.contrib import messages
# from .models import Booking


def index(request):
    return render(request, 'index.html')

def doctor_list(request):
    return render(request, 'dr_list.html')

def contact(request):
    return render(request, 'contact.html')

def ai_bot(request):
    return render(request, 'AI BOT.html')


from django.shortcuts import render, redirect
from .models import Appointment
from django.shortcuts import get_object_or_404

def appointment_view(request):
    doctors = Doctor.objects.all()
    if request.method == "POST":
        doctor_id = request.POST.get("doctor")  # will be like "1"
        doctor_instance = get_object_or_404(Doctor, id=doctor_id)

        Appointment.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            date=request.POST.get("date"),
            time=request.POST.get("time"),
            doctor=doctor_instance,
            message=request.POST.get("message")
        )
        return redirect('booking_list')  # redirect after successful booking

    return render(request, 'booking.html', {'doctors': doctors})

def booking_list(request):
    bookings = Appointment.objects.select_related('doctor').all().order_by('-date')
    return render(request, 'booking_list.html', {'bookings': bookings})


def blog_single(request):
    return render(request, 'blog-single.html')
def portfolio_details(request):
    return render(request, 'portfolio-details.html')