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

def logoutPage(request):
    logout(request)
    return redirect('loginPage')



# @login_required(login_url='login')
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

# @login_required(login_url='login')
def about(request):
    return render(request, 'gurukul_app/about.html')



def ihome(request):
    course = Course.objects.all
    context = {
        'course': course,
    }
    return render(request,"ihome.html",context)

def myCourse(request):
    quizes = Quiz.objects.all
    context = {
        'quizes':quizes,
    }
    return render(request,"myCourse.html",context)

def contribute(request):
    return render(request,"contribute.html")

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
        return render(request, 'quiz.html', context)


def addQuestion(request):
    #if request.user.is_staff:
    form=addQuestionform()
    if(request.method=='POST'):
        form=addQuestionform(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('addQuestion')
    context={'form':form}
    return render(request,'addQuestion.html',context)
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
    return render(request, 'addQuiz.html', context)
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
    return render(request, 'createCourse.html', context)
    # else:
    #     return render(request, "home.html")

def courses(request):
    course = Course.objects.all
    context={
        'course':course,
    }
    return render(request,"courses.html",context)

def courseDescription(request):
    coursedesc = Course.objects.all
    context = {
        'coursedesc':coursedesc
    }
    return render(request,"courseDescription.html",context)


def index(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"dashboard.html")

def myCourses(request):
    return render(request,"myCourses.html")

def tests(request):
    quizes = Quiz.objects.all
    context = {
        'quizes': quizes
    }
    return render(request, "tests.html", context)
