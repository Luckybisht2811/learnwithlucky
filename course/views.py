from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from collections import defaultdict
from .models import Note, Course
from django.core.mail import send_mail
from django.contrib import messages
import json
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache  # ← add this

def home(req):
    return render(req, 'course/home.html', {
        'courses_json': '[]',
        'notes_json': '[]',
    })

# Course
def courses(req):
    # check cache first
    all_courses = cache.get('all_courses')

    if not all_courses:
        all_courses = list(Course.objects.all())
        cache.set('all_courses', all_courses, timeout=300)  # cache for 5 minutes

    courses_json = json.dumps([
        {
            "title": c.title,
            "url": f"/courses/{c.id}/"
        }
        for c in all_courses
    ])
    return render(req, 'course/courses.html', {
        'courses': all_courses,
        'courses_json': courses_json,
        'notes_json': '[]',
    })

@login_required(login_url='/register/')
def course_detail(request, course_id):
    # cache each course separately by id
    cache_key = f'course_{course_id}'
    course = cache.get(cache_key)

    if not course:
        course = Course.objects.get(id=course_id)
        cache.set(cache_key, course, timeout=300)

    return render(request, 'course/course_detail.html', {
        'course': course,
        'courses_json': '[]',
        'notes_json': '[]',
    })

# Notes
def notes(req):
    # check cache first
    all_notes = cache.get('all_notes')

    if not all_notes:
        all_notes = list(Note.objects.all())
        cache.set('all_notes', all_notes, timeout=300)  # cache for 5 minutes

    grouped_notes = defaultdict(list)
    for note in all_notes:
        grouped_notes[note.language].append(note)

    notes_json = json.dumps([
        {
            "title": n.title,
            "url": f"/notes/{n.id}/"
        }
        for n in all_notes
    ])
    return render(req, 'course/notes.html', {
        'grouped_notes': dict(grouped_notes),
        'notes_json': notes_json,
        'courses_json': '[]',
    })


# Contact
def contact(req):
    if req.method == 'POST':
        name    = req.POST.get('name')
        email   = req.POST.get('email')
        message = req.POST.get('message')

        subject = f"New Message from {name} | LearnWithLucky Contact"
        body = f"""
You received a new message from your website contact form.

Name    : {name}
Email   : {email}

Message :
{message}
        """

        try:
            send_mail(
                subject,
                body,
                email,
                ['lalitsinghbisht282002@gmail.com'],
                fail_silently=False,
            )
            messages.success(req, '✅ Your message has been sent successfully! I will get back to you soon.')
        except Exception as e:
            messages.error(req, '❌ Something went wrong. Please try again later.')

    return render(req, 'course/contact.html', {
        'courses_json': '[]',
        'notes_json': '[]',
    })


# Login Section
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'course/login.html', {'error': 'Invalid email or password'})

    return render(request, 'course/login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'course/register.html', {'error': 'Passwords do not match'})
        if User.objects.filter(username=username).exists():
            return render(request, 'course/register.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'course/register.html', {'error': 'Email already registered'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'course/register.html')


# Search
def search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'course/search.html', {'results': results, 'query': query})