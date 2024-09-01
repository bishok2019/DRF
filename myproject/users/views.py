from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the user to the database
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('myapp/blog-home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('blog-home')
#     # message={"hello":"welcome"}
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            myuser = User.objects.create_user(username=username, password=password, email=email)
            myuser.save()
            #username = 
            messages.success(request, "Registration Success!")
            return redirect('blog-home')
        except IntegrityError:
            messages.error(request, "Username already exists. Please choose another username.")
            return render(request, "register.html")
    else:
        return render(request, "register.html")


# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')

#         if not all([username, email, password, cpassword]):
#             error_message = 'All fields are required'
#             return render(request, 'register.html', {'error_message': error_message})

#         if password != cpassword:
#             error_message = 'Passwords do not match'
#             return render(request, 'register.html', {'error_message': error_message})

#         try:
#             validate_password(password)
#         except ValidationError as e:
#             return render(request, 'register.html', {'error_message': e.messages})

#         try:
#             if User.objects.filter(username=username).exists():
#                 error_message = 'Username already taken'
#                 return render(request, 'register.html', {'error_message': error_message})

#             if User.objects.filter(email=email).exists():
#                 error_message = 'Email already registered'
#                 return render(request, 'register.html', {'error_message': error_message})

#             user = User.objects.create_user(username, email, password)
#             user.save()
#             login(request, user)
#             return redirect('index')  # Assuming 'index' is the name of your home page URL pattern
#         except Exception as e:
#             error_message = f'Error creating account: {str(e)}'
#             return render(request, 'register.html', {'error_message': error_message})

#     return render(request, 'register.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         if not username or not password:
#             error_message = 'Both username and password are required'
#             return render(request, 'login.html', {'error_message': error_message})

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')  # Assuming 'index' is the name of your home page URL pattern
#         else:
#             error_message = "Invalid username or password"
#             return render(request, 'login.html', {'error_message': error_message})

#     return render(request, 'login.html')

# def user_logout(request):
#     logout(request)
#     messages.success(request, "Logged out successfully!")
#     return redirect('login')  
