from django.db import models

class EmployeeFeedback(models.Model):

    employee_name = models.CharField(max_length=150)

    employee_id = models.CharField(max_length=20, unique=True)

    department = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=10)

    joining_date = models.DateField()

    experience = models.PositiveIntegerField()

    feedback = models.TextField()

    recommendations = models.TextField()

    def __str__(self):
        return self.employee_name