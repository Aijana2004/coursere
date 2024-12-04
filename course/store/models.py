from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('преподаватель', 'преподаватель'),
        ('студент', 'студент'),
        ('админ', 'админ'),

    )
    user_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='студент')
    STATUS_CHOICES = (
        ('simple', 'simple'),
        ('premium', 'premium'),

    )
    status = models.CharField(max_length=32,choices=STATUS_CHOICES,default='simple')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='user_images/')
    bio = models.TextField()


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Course(models.Model):
    course_name = models.CharField(max_length=60,unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),

    )
    level = models.CharField(max_length=22,choices=LEVEL_CHOICES)
    price = models.PositiveSmallIntegerField()
    created_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f'{self.course_name} - {self.description}'


class Lesson(models.Model):
    title = models.CharField(max_length=35)
    content = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class CourseVideo(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    lesson_video = models.ForeignKey(Lesson,on_delete=models.CASCADE)


class Assignment(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    due_data = models.DateField(verbose_name='срок сдачи')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    students = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.due_data} - {self.students}'


# class Questions(models.Model):
#     questions = models.TextField()
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#

class Exam(models.Model):
    exam_name = models.CharField(max_length=40)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    # questions = models.ForeignKey(Questions)
    questions = models.TextField()
    passing_score = models.PositiveSmallIntegerField(verbose_name='проходной балл')
    duration = models.DurationField(verbose_name='Время на выполнение')

    def __str__(self):
        return f'{self.exam_name} - {self.course}'


class Certificate(models.Model):
    student = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    course = models.OneToOneField(Course,on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField(verbose_name='сертификат',null=True,blank=True)

    def __str__(self):
        return f'{self.student}'


class CourseReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course_reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.course} - {self.rating}'


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='favorite_user')
    favorite_course = models.ManyToManyField(Course)
    created_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='cart')

    def __str__(self):
        return f' {self.user}'


class CarItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    # quantity = models.PositiveSmallIntegerField(default=1)















