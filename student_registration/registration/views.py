from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('registration_success')
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration/student_registration.html', {'form': form})


def registration_success(request):
    return render(request, 'registration/registration_success.html')



