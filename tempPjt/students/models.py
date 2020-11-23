from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=100)
    s_major = models.CharField(max_length=100)
    s_age = models.IntegerField(default=0)
    s_grade = models.IntegerField(default=0)
    s_gender = models.CharField(max_length=30)

    def __str__(self):
        return self.s_name



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') #pub_date 컬럼에 대한 레이블 문구
    
    #객체를 문자열로 표한할때 사용하는 함수
    #Admin 사이트나 장고 쉘등에서 테이블명을 표시
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#id변수 지정할 필요없이 클래스만 지정하면된다, _id 붙는다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text