from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
from .forms import ContactForm
from django.contrib import messages
def home(request):
    events = Event.objects.all().order_by('-date')[:5]
    news = News.objects.all().order_by('-date')[:5]
    calendar_events = CalendarEvent.objects.all().order_by('date')
    background_images = BackgroundImage.objects.all().order_by('order')
    return render(request, 'home.html', {
        'events': events,
        'news': news,
        'calendar_events': calendar_events,
        'background_images': background_images,
    })

def about(request):
    about = About.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name}',
                message,
                email,
                [about.email],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        form = ContactForm()
    return render(request, 'about.html', {'about': about, 'form': form})
  
 
def administration(request):
    administrators = Administrator.objects.all().order_by('order')
    return render(request, 'administration.html', {'administrators': administrators})

def teaching_staff(request):
    staff = TeachingStaff.objects.all().order_by('order')
    return render(request, 'teaching_staff.html', {'staff': staff})

def achievements(request):
    university_admissions = Achievement.objects.all().order_by('year')
    awards = CoCurricularAward.objects.all().order_by('-year')
    return render(request, 'achievements.html', {
        'university_admissions': university_admissions,
        'awards': awards,
    }) 

def holiday_assignments(request):
    assignments = HolidayAssignment.objects.all().order_by('-date_uploaded')
    return render(request, 'holiday_assignments.html', {'assignments': assignments})

def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'news_detail.html', {'news': news})