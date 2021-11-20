from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .forms import CreateUserForm

import jwt
import requests
import json
from time import time
  
  
# Enter your API key and your API secret
API_KEY = 'luG0QRRMRbKD0TVFS1ogBA'
API_SEC = '87vfsjgsBhmwHIOVwC8gVsplhhFqDVNpEfLN'
  


def beforeLogin(request):
    return render(request, 'gurukul_app/beforeLogin.html')



def sregisterPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('sloginPage')
			

		context = {'form':form}
		return render(request, 'gurukul_app/sregisterPage.html', context)

def sloginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'gurukul_app/sloginPage.html', context)

def slogoutUser(request):
	logout(request)
	return redirect('sloginPage')

def registerPage(request):

    form=registerationform()
    if request.method=='POST':
        form=registerationform(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('loginPage')
    context={
            'form':form,
    }
    return render(request,'gurukul_app/registerPage.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        print("ii")
        return redirect('ihome')
    else:
        print("else")
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        
        context = {}
        return render(request, 'gurukul_app/loginPage.html', context)

# @login_required(login_url='sloginPage')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')



# @login_required(login_url='sloginPage')
def home(request):
    course = Course.objects.all
    context = {
        'course': course,
    }
    return render(request,"gurukul_app/home.html",context)

# @login_required(login_url='login')
def courses(request):
    course = Course.objects.all
    context={
        'course':course,
    }
    return render(request,"gurukul_app/courses.html",context)	

# @login_required(login_url='login')
def createCourse(request):
    # if request.user.is_staff:
        form = createCourseform()
        if (request.method == 'POST'):
            form = createCourseform(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('courses')
        context = {'form': form}
        return render(request, 'gurukul_app/createCourse.html', context)
    # else:
    #     return render(request, "gurukul_app/home.html")


# @login_required(login_url='login')
def courseDescription(request, id):
    coursedesc = Course.objects.get(id = id)
    context = {
        'coursedesc':coursedesc
    }
    return render(request,"gurukul_app/courseDescription.html",context)

@login_required(login_url='login')
def about(request):
    return render(request, 'gurukul_app/about.html')



def ihome(request):
    course = Course.objects.all
    context = {
        'course': course,
    }
    return render(request,"gurukul_app/ihome.html",context)

def myCourse(request):
    quizes = Quiz.objects.all
    context = {
        'quizes':quizes,
    }
    return render(request,"myCourse.html",context)

def contribute(request):
    return render(request,"gurukul_app/contribute.html")

def quiz(request,id):
    if request.method == 'POST':
        print(request.POST)
        quiz = Quiz.objects.get(id=id)
        questions= Question.objects.filter(quiz=quiz,quiz_id=id)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        course = Quiz.objects.get(id=id)
        questions = Question.objects.filter(quiz=course,quiz_id=id)
        context = {
            'questions': questions,
            'id':id
        }
        return render(request, 'gurukul_app/quiz.html', context)


def addQuestion(request):
    #if request.user.is_staff:
    form=addQuestionform()
    if(request.method=='POST'):
        form=addQuestionform(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('addQuestion')
    context={'form':form}
    return render(request,'gurukul_app/addQuestion.html',context)
    #else:
        #return render(request,"home.html")


def addQuiz(request):
    #if request.user.is_staff:
    form = addCourseform()
    if (request.method == 'POST'):
        form = addCourseform(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('addQuestion')
    context = {'form': form}
    return render(request, 'gurukul_app/addQuiz.html', context)
    #else:
        #return render(request, "home.html")

def createCourse(request):
    # if request.user.is_staff:
    form = createCourseform()
    if (request.method == 'POST'):
        form = createCourseform(request.POST)
        if (form.is_valid()):
             form.save()
             return redirect('courses')
    context = {'form': form}
    return render(request, 'gurukul_app/createCourse.html', context)
    # else:
    #     return render(request, "home.html")

def courses(request):
    course = Course.objects.all
    context={
        'course':course,
    }
    return render(request,"gurukul_app/courses.html",context)

def courseDescription(request):
    coursedesc = Course.objects.all
    context = {
        'coursedesc':coursedesc
    }
    return render(request,"gurukul_app/courseDescription.html",context)


def index(request):
    return render(request,"gurukul_app/index.html")

def dashboard(request):
    return render(request,"gurukul_app/dashboard.html")

def myCourses(request):
    return render(request,"gurukul_app/myCourses.html")

def tests(request):
    quizes = Quiz.objects.all
    context = {
        'quizes': quizes
    }
    return render(request, "gurukul_app/tests.html", context)


def generateToken():
    token = jwt.encode(
        
        # Create a payload of the token containing 
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},
          
        # Secret used to generate token signature
        API_SEC,
          
        # Specify the hashing alg
        algorithm='HS256'
    )
    return token
  
  
# create json data for post requests
meetingdetails = {"topic": "The title of your zoom meeting",
                  "type": 2,
                  "start_time": "2019-06-14T10: 21: 57",
                  "duration": "45",
                  "timezone": "Europe/Madrid",
                  "agenda": "test",
  
                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }
  
# send a request with headers including 
# a token and meeting details
def createMeeting():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings', 
      headers=headers, data=json.dumps(meetingdetails))
  
    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]
    tr=json.dumps(join_URL)
    print(
        f'\n here is your zoom meeting link {join_URL} and your \
        password: "{meetingPassword}"\n')
    print(type(tr))
    context = {
        'url': tr
    }
    return render("gurukul_app/vediochat.html",context)  

  
  
# run the create meeting function
createMeeting()
 