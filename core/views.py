from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Result, Blog, Admission, Certificate

# Create your views here.


def home(request):
    return render(request, "website/index.html")


@login_required(login_url="login_page_site")
def result(request):
    student_result = Result.objects.all()
    if request.method == "POST":
        search_result = request.POST.get("resultSearch")
        student_result = Result.objects.filter(name__icontains=search_result)

    context = {"results": student_result, "page_title": "Let see your results | UPSY"}
    return render(request, "website/result.html", context=context)


@login_required(login_url="login_page_site")
def admission(request):
    context = {"page_title": "Let's get a admission"}
    if request.method == "POST":
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        father_name = request.POST.get("father-name")
        student_cnic = request.POST.get("stud_cnic")
        student_contact = request.POST.get("contact-number")
        stud_field = request.POST.get("stud_field")
        student_details = Admission.objects.create(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            student_cnic=student_cnic,
            contact_number=student_contact,
            student_field=stud_field,
        )
        student_details.save()
        return redirect("Admission")
    return render(request, "website/admission.html", context=context)


@login_required(login_url="login_page_site")
def blog(request):
    school_blog = Blog.objects.all()
    context = {"page_title": "Our Blogs | UPSY", "school_blogs": school_blog}
    return render(request, "website/blog.html", context)


@login_required(login_url="login_page_site")
def blog_detail(request, pk):
    school_blogs_site = Blog.objects.filter(uuid_num=pk)

    context = {"page_title": "Blog detail | UPSGY", "school_blogs": school_blogs_site}
    return render(request, "website/blog-detail.html", context=context)


def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials invalid")
            return redirect("login_page_site")
    return render(request, "website/login.html", context={"page_title": "Login to s"})


def sign_up(request):
    if request.method == "POST":
        profile_image = request.POST.get("profile_image")
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("sign-up_page")
        elif User.objects.filter(username=username).exists():
            messages.info(request, "username already taken")
        else:
            user_reg = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user_reg.save()
            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)

            return redirect("/")
    return render(
        request, "website/sign-up.html", context={"page_title": "create your account"}
    )


def logout(request):
    auth.logout(request)
    return redirect("login_page_site")


@login_required(login_url="login_page_site")
def stud_result(request, pk):
    stud_result_details = Result.objects.filter(uuid_num=pk)
    context = {"stud_result_details": stud_result_details}
    return render(request, "website/result_details.html", context)


@login_required(login_url="login_page_site")
def certificate(request):
    print(request.user)
    user_certificate = Certificate.objects.filter(user=request.user)
    context = {
        "page_title": "Get your certificate online",
        "user_certificates": user_certificate,
    }
    return render(request, "website/certificate.html", context=context)
