from django.shortcuts import render
from .forms import EmployeeFeedbackForm

def employee_feedback(request):

    if request.method == "POST":
        form = EmployeeFeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "success.html")

    else:
        form = EmployeeFeedbackForm()

    return render(request, "employee_form.html", {"form": form})