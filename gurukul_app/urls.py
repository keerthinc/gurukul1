from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.beforeLogin, name="beforeLogin"),
    path('home',views.home,name="home"),
    path('ihome/',views.ihome,name="ihome"),
    path('myCourse/',views.myCourse,name="myCourse"),
    path('<id>',views.quiz,name="quiz"),
    path('addQuestion/',views.addQuestion,name="addQuestion"),
    path('addQuiz/',views.addQuiz,name="addQuiz"),
    path('index/',views.index,name="index"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('myCourses/',views.myCourses,name="myCourses"),
    path('tests/',views.tests,name="tests"),
    path('loginPage/', views.loginPage,name='loginPage'),
    path('contribute/', views.contribute,name='contribute'),
    path('sregisterPage/',views.sregisterPage,name="sregisterPage"),
    path('slogin/',views.sloginPage,name="sloginPage"),
    path('registerPage/', views.registerPage,name='registerPage'),
    path('login/', views.login,name='login'),
    path('createCourse/',views.createCourse,name='createCourse'),
    path('courses/',views.courses,name='courses'),
    path('courseDescription/',views.courseDescription,name='courseDescription'),
    path('logoutPage/',views.logoutPage,name='logoutPage'),
]
