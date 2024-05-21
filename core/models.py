from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    uuid_num = models.UUIDField(default=uuid.uuid4)
    blog_image = models.ImageField(upload_to="blog_image/")
    blog_title = models.CharField(max_length=100, default="Blog title")
    blog_description = models.TextField(default="blog description")

    def __str__(self) -> str:
        return self.blog_title


class Result(models.Model):
    uuid_num = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    student_section = models.CharField(max_length=100)
    English = models.CharField(max_length=100, default="None")
    Urdu = models.CharField(max_length=100, default="None")
    Math = models.CharField(max_length=100, default="None")
    Chemistry = models.CharField(max_length=100, default="None")
    Science = models.CharField(max_length=100, default="None")
    SST_book = models.CharField(max_length=100, default="None")
    Islamiat = models.CharField(max_length=100, default="None")
    Computer = models.CharField(max_length=100, default="None")
    Biology = models.CharField(max_length=100, default="None")
    Total_marks = models.IntegerField(default=0)
    Percentage = models.CharField(max_length=100, default="0%")

    def __str__(self):
        return self.name


class Admission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    student_cnic = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    student_field = models.CharField(max_length=100, default="lower than 9th class")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Certificate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    certificate_image = models.ImageField(upload_to="certificate/")

    def __str__(self) -> str:
        return self.user.get_username()
