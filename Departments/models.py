
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Departments(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='Department_pics',default='')

    def __str__(self):
        return self.name

    def save(self):
        super().save() #saves image first
        img=Image.open(self.image.path) #opens image using self
        if img.height>300 or img.width>300:
            resized_img=(300,300)
            img=img.resize(resized_img)

class Courses(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField()
    course_structure = models.TextField()
    admission_requirement = models.TextField()
    fee_structure = models.FileField(upload_to='fee_structure_pics',null=True)
    # student = models.ForeignKey('Students', on_delete=models.CASCADE,null=True)
    department = models.ForeignKey(Departments,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='Department_pics',default='')

    def __str__(self):
        return self.name

    # def save(self):
    #     super().save() #saves image first
    #     img=Image.open(self.image.path) #opens image using self
    #     if img.height>300 or img.width>300:
    #         resized_img=(300,300)
    #         img=img.resize(resized_img)


class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True)
    second_name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    service_no = models.CharField(max_length=100, null=True)
    id_no = models.IntegerField(null=True,blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True, related_name='students')
    profile_pic=models.ImageField(upload_to='profile_pics',null=True,blank=True,default='/Edu.jpg')

    qualifications = models.FileField()
    address = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        if self.user:
            return self.user.username
        return f"Student {self.pk}"

    def save(self):
        super().save() #saves image first
        img=Image.open(self.profile_pic.path) #opens image using self
        if img.height>300 or img.width>300:
            resized_img=(300,300)
            img=img.resize(resized_img)

class News(models.Model):
    image=models.ImageField(upload_to='news_pics',default='')
    Title=models.CharField(max_length=100, null=True)
    content=models.TextField()
    puplish_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    # def save(self):
    #     super().save() #saves image first
    #     img=Image.open(self.image.path) #opens image using self
    #     if img.height>300 or img.width>300:
    #         resized_img=(300,300)
    #         img=img.resize(resized_img)

class FAQ(models.Model):
    Question=models.TextField()
    Answer=models.TextField()

    def __str__(self):
        return self.Question

class Location_Info(models.Model):
    Email=models.EmailField()
    phone_no=models.CharField(max_length=15)
    pysical_address=models.TextField()
    Electronic_Address=models.TextField()

    def __str__(self):
        return self.Electronic_Address

class About_Us(models.Model):
    VisionAndValues=models.TextField()
    VisionAndValues_image=models.ImageField(upload_to='VisionAndValues_pics',null=True,blank=True)
    Our_Qualities=models.CharField(max_length=100)
    History=models.TextField()
    History_image=models.ImageField(upload_to='History_pics',null=True,blank=True)

    # def save(self):
    #     super().save() #saves image first
    #     img=Image.open(self.VisionAndValues_image.path) #opens image using self
    #     img2=Image.open(self.History_image.path)
    #     if (img.height>300 or img.width>300) or (img2.height>300 or img2.width>300):
    #         resized_img=(300,300)
    #         img=img.resize(resized_img)
    #         img2=img2.resize(resized_img)

