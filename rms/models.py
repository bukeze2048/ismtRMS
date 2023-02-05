from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    matric_number = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    current_cgpa = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    grade = models.CharField(max_length=2)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
