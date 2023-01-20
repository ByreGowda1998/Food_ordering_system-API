from django.shortcuts import render,redirect
from app_login.forms import ContactForm,Profile_form
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.forms import AuthenticationForm
from app_login.forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login ,logout,authenticate 
from app_login.models import User,Profile
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.


# Home Page
def homepage(request):
    return render(request,'app_login/home.html')

# About Page
def aboutus(request):
    return render (request ,'app_login/aboutus.html')

# Contact Page
def contact_us(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message =request.POST.get('message')
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
               'Enquirey form',
               f"{message}",
               f'{email}',
               ['fooddeliver@gmail.com'])
            messages.info(request, 'your message sent to the fooddeliver@gmail.com')
            return render(request, 'app_login/contact.html')
    contact_form=ContactForm()
    return render (request,'app_login/contact.html',{'contact_form':contact_form})





#Log in Page

def loginto(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, "You are now login is succesfull")
				return redirect("home")
		else:
				messages.error(request,"Invalid username or password.")    
	form = AuthenticationForm()
	return render(request=request, template_name='app_login/login.html', context={"login_form":form})  






# User Registrtion page

def user_register(request):
    if request.method == "POST":
        user_form = NewUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("loginto")
        else:
            print(user_form.errors)
        messages.error(request,user_form.errors,'pls enter valid information and password')
    user_form = NewUserForm()
    return render (request,"app_login/register.html", context={"user_reg_form":user_form})





# LOGOUT
@login_required(login_url='loginto')     
def log_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("loginto")


# User Profile Page
def Profile(request):
    if request.method == 'POST':
        form = Profile_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile created." )
            return render(request, 'app_login/profilepage.html')
    form = Profile_form()
    return render(request,'app_login/profilepage.html',{'profile_form':form})

