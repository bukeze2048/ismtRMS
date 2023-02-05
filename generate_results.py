from django.core.management.base import BaseCommand
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from django.http import FileResponse
from io import BytesIO
from xhtml2pdf import pisa

class Command(BaseCommand):
    help = 'Generates PDF results for each department and each student'

    def handle(self, *args, **kwargs):
        departments = Department.objects.all()
        for department in departments:
            students = Student.objects.filter(department=department)
            context = {'department': department, 'students': students}
            template = get_template('results/department_pdf.html')
            html = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            if not pdf.err:
                response = FileResponse(result, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="{}_results.pdf"'.format(department.code)
                print(response)
            else:
                print("Error generating PDF for department: {}".format(department.code))

        students = Student.objects.all()
        for student in students:
            results = Result.objects.filter(student=student)
            context = {'student': student, 'results': results}
            template = get_template('results/student_pdf.html')
            html = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            if not pdf.err:
                response = FileResponse(result, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="{}_results.pdf"'.format(student.matric_number)
                print(response)
            else:
                print("Error generating PDF for student: {}".format(student.matric_number))
