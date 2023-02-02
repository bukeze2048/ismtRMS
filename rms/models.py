from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.firl
class StudentClass(models.Model):
    level = models.CharField(max_length=25, help_text='Eg: 100 Level, 200Level etc')
    session = models.CharField(max_length=25, help_text='Eg: 2022/2023')

    def get_absolute_url(self):
        return reverse('student_classes:class_list')
    
    def __str__(self):
        return '%s Academic_Session-%s'%(self.level, self.session)

class Faculty(models.Model):
    name = models.CharField(max_length=100)
class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    matric_number = models.Charfield(max_length=50)

class Course(models.Model):
    course = models.Charfield(max_length=100)
    course_code = models.CharField(max_length=10)
class Results(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(course)