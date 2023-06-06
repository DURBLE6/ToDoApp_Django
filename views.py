from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from scheduleapp.models import Task, User





# Create your views here.
def home(request):
    if request.method == 'POST':
        #retrieve user's details from the form
        email = request.POST['email']
        pwd = request.POST['password']

        #check if the details are correct
        user = User.objects.get(email=email)
        if check_password(pwd, user.password):
            request.session['user']=user.id
            request.session.save()
            messages.success(request, 'Login successful')
            return redirect('alltasks')
        else:
            messages.error(request,'Username or password incorrect')
            return render('homepage')
            
    else:
        return render(request, 'scheduleapp/homepage.html')



@csrf_protect
def register(request):
    if request.method == 'POST':
        #retrieve user's data from the form
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_p = request.POST['password-2']

        #verify if both passwwords matches
        if email!= "" and f_name!="" and l_name!="" and password!="" and confirm_p:

            #since the username/email constraint is set to be unique in the models, query the database to check if the coming email has not been registered before
            if User.objects.filter(email = email).exists():
                messages.error(request, 'User already exist with the username, you may want to reset your password if you have forgotten')
                return redirect('register')
            else:
                if password == confirm_p:
                    #hash the password before saving to the database
                    harsh_password = make_password(password)

                    #query the database to save the data from the form
                    users = User.objects.create(first_Name=f_name, last_Name=l_name, email=email, password=harsh_password)
                    users.save()
                    messages.success(request, 'Registration successful')
                    return redirect('notifications')
                else:
                    messages.info('password doesn\'t match')
                    return redirect('register')
        else:
            messages.error(request, 'Please complete the form')
            return redirect('register')
    else:
        return render(request, 'scheduleapp/signuppage.html')



def alltask(request):
    if request.session['user']!= None:
        user = User.objects.get(id = request.session['user'])
        task = Task.objects.filter(user = user).all()
        return render(request, 'scheduleapp/alltasks.html', {
        'tasks':task,
        'users':user,
        })
    else:
        return render(request, 'scheduleapp/homepage.html') 



def dashboard(request, task_title):
    if request.session['user']!= None:
        task = Task.objects.get(title=task_title)
        users = User.objects.get(id = request.session.get('user'))
        return render(request, 'scheduleapp/dashboard.html', {
        'task':task,
        'user':users})
    else:
        return render(request, 'scheduleapp/homepage.html')

def complete(request, id):
    if request.session['user'] !=  None:
        if request.method == 'POST':
            update = request.POST.get('taskupdate')
            task = Task.objects.get(id=id)
            task.status = update
            task.save()
            return redirect('alltasks')
    else:
        return redirect('home')



def new_task(request):
    if request.session['user'] != None:
        if request.method == 'GET':
            user = User.objects.filter(id = request.session['user']).first()
            return render(request, 'scheduleapp/newtask.html', { 'user':user })

        else:
            if request.method == 'POST':
                title = request.POST.get('title')
                note = request.POST.get('note')
                date = request.POST.get('date')
                user = User.objects.filter(id = request.session['user']).first()

                if title and date:
                    new_task = Task.objects.create(title = title, notes = note, date = date, user = user)
                    messages.success(request, 'Task created successfully')
                    return redirect('notifications')
                else:
                    messages.info(request,'Please complete the fields')
                    return redirect('new_task')
    else:
        return redirect('home')



def notifications(request):
    if request.session['user']!= None:
        return render(request, 'scheduleapp/task_notification.html')
    else:
        return render(request, 'scheduleapp/signin_notification.html')



def delete(request, title):
    if request.session['user']!=None:
        task = get_object_or_404(Task, title=title)
        task.delete()
        return redirect('alltasks')




@login_required
def signout(request):
    if 'user' in request.session:
        request.session.pop('user', None)
        messages.success(request, 'successfully logged out')
        return redirect('home')
