from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is exist ')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,
                                                password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                print("success")
                return redirect('login_user')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        print("no post method")
        return render(request, 'signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index.html')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('index.html')


def forms(request):
    return render(request, 'forms.html')


def selldeed(request):
    return render(request, 'sell_deed.html')


def agreement(request):
    return render(request, 'agreement.html')


def tax(request):
    return render(request, 'tax.html')


def documents(request):
    return render(request, 'documents.html')


def registration(request):
    return render(request, 'registration.html')


def applicationstatus(request):
    return render(request, 'track_application.html')

# def check_status(request):
#     if request.method == 'POST':
#         reference_id = request.POST.get('reference_id')
#         # Logic to check the status of the application using the reference ID
#         # You can query the database or perform any other necessary operations
#         # and retrieve the status based on the provided reference ID.
#         # For demonstration purposes, let's assume the status is retrieved as 'Pending'.
#         status = 'Pending'
#         return render(request, 'application_status.html', {'application_status': status})
#     return render(request, 'application_status.html')
