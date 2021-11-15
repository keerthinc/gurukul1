from django.db import models

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)

    def __str__(self):
        return self.quiz_name



class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100,blank=True)
    opt4 = models.CharField(max_length=100,blank=True)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    duration = models.IntegerField()
    #image = models.ImageField()
    ratings = models.FloatField()
    description = models.TextField()
    company = models.CharField(max_length=250)

    def __str__(self):
        return self.course_name

class register(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=250)
    password1 = models.CharField(max_length=250)
    password2 = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    specialization = models.CharField(max_length=250)

    def __str__(self):
        return self.email



