from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RegisterForm, StudentForm
from .models import Student

def home(request):
    return render(request, "students/home.html")

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome aboard! Your account is ready.")
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def dashboard(request):
    qs = Student.objects.all() if request.user.is_staff else Student.objects.filter(created_by=request.user)
    context = {
        "student_count": qs.count(),
        "course_count": qs.values("course").distinct().count(),
        "recent_students": qs[:5],
        "is_staff": request.user.is_staff,
    }
    return render(request, "students/dashboard.html", context)

@login_required
def student_list(request):
    qs = Student.objects.all() if request.user.is_staff else Student.objects.filter(created_by=request.user)
    query = request.GET.get("q", "").strip()
    if query:
        qs = qs.filter(
            Q(student_id__icontains=query) | Q(full_name__icontains=query) |
            Q(email__icontains=query) | Q(course__icontains=query)
        )
    return render(request, "students/student_list.html", {"students": qs, "query": query})

@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_by = request.user
            student.save()
            messages.success(request, f"{student.full_name} was added successfully.")
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {"form": form, "heading": "Add a student", "button": "Save student"})

@login_required
@user_passes_test(lambda u: u.is_staff)
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student details updated.")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "students/student_form.html", {"form": form, "heading": "Edit student", "button": "Update student"})

@login_required
@user_passes_test(lambda u: u.is_staff)
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        name = student.full_name
        student.delete()
        messages.success(request, f"{name} was deleted.")
        return redirect("student_list")
    return render(request, "students/student_confirm_delete.html", {"student": student})
