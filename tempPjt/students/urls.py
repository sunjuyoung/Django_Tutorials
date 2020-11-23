from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('reg/', views.regStudent, name='reg'),
    path('regCon/', views.regConStudent, name='regCon'),
    path('all/', views.readStudentAll, name='stuAll'),
    path('polls/',views.index, name='index'),
    path('polls/<int:question_id>/',views.detail, name='detail'),
    #path('polls/<int:question_id>/results/',views.results, name='results'),
    #path('polls/<int:question_id>/vote/',views.vote, name='vote'),
]
