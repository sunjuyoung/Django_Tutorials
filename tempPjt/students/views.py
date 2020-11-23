from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student,Question,Choice


#등록화면
def regStudent(request):
    return render(request,'students/registerStudent.html')

#등록
def regConStudent(request):
    name=request.POST['name']
    age=request.POST['age']
    major=request.POST['major']
    grade=request.POST['grade']
    gender=request.POST['gender']

    qs = Student(s_name=name,s_age=age,s_major=major,s_grade=grade,s_gender=gender)
    qs.save()
    return HttpResponseRedirect(reverse('students:stuAll'))

#전제리스트
def readStudentAll(request):
    qs = Student.objects.all()
    context = {'student_list':qs}
    return render(request,'students/readStudents.html',context)


#설문 화면
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

#설문 디테일
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)#단축함수 사용
    return render(request,'polls/detail.html',{'question':question})