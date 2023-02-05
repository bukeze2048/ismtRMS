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
    grade = models.CharField(max_length=2, blank=True)
    semester = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.score >= 0 and self.score <= 39:
            self.grade = 'F'
        elif self.score >= 40 and self.score <= 49:
            self.grade = 'D'
        elif self.score >= 50 and self.score <= 59:
            self.grade = 'C'
        elif self.score >= 60 and self.score <= 69:
            self.grade = 'B'
        elif self.score >= 70 and self.score <= 100:
            self.grade = 'A'
        else:
            raise ValueError('Score must be between 0 and 100')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
