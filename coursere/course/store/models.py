from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# from django.core.validators import MinValueValidator, MaxValueValidator
# from multiselectfield import MultiSelectField

class Online_Examination_System(models.Model):
    instructions=models.CharField(max_length=500)


class UserProfile(AbstractUser):
    Address = models.CharField(max_length=100)
    Phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    Profile_picture = models.ImageField(upload_to='user_images/')
    Bio = models.TextField()
    Test_date = models.DateField(auto_now_add=True)
    Student_No = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


# class Teacher(models.Model):



class Course(models.Model):
    course_name = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),

    )
    STATUS_CHOICES = (
        ('free', 'free'),
        ('premium', 'premium'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='free')
    choice_level = models.CharField(max_length=22, choices=LEVEL_CHOICES)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f'{self.course_name},{self.choice_level}'


class CourseVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_video')
    course_video = models.FileField(upload_to='course_video/')
    course_image = models.ImageField(upload_to='course_image/')
    course_data = models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=35)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f'{self.lesson_name},{self.course}'


class LessonVideo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lessons')
    lesson_video = models.FileField(upload_to='lesson_video/')
    lesson_image = models.ImageField(upload_to='lesson_image/')
    lesson_data = models.DateTimeField(auto_now_add=True)


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=40)
    description = models.TextField()
    due_data = models.DateField(verbose_name='срок сдачи')
    mark_rules = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.assignment_name} , {self.course} , {self.students}'


class Courses(models.Model):
    curses_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.curses_name}'


class Exam(models.Model):
    exam_name = models.CharField(max_length=40)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='exams')
    exam_date = models.DateTimeField(auto_now_add=True)
    passing_score = models.PositiveSmallIntegerField(verbose_name='проходной балл')
    duration = models.DurationField(verbose_name='Время на выполнение')

    DIFFICULTY_LEVEL = (
        ('сложный', 'сложный'),
        ('средний', 'средний'),
        ('легкий', 'легкий'),
    )
    level_status = models.CharField(max_length=32, choices=DIFFICULTY_LEVEL, default='средний')

    def __str__(self):
        return f'{self.exam_name} , {self.course}'


class Questions(models.Model):
    topic_name = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='questions')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='questions')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    Option_A = models.CharField(max_length=255)
    Option_B = models.CharField(max_length=255)
    Option_C = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')], )
    correct_option = models.CharField(max_length=1, choices=[("A", "Option A"), ("B", "Option B"), ("C", "Option C")],
                                      )

    def __str__(self):
        return f'{self.topic_name},{self.user},{self.course},{self.text}'


class Certificate(models.Model):
    student = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField(verbose_name='сертификат', null=True, blank=True)

    def __str__(self):
        return f'{self.student}'


class CourseReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} , {self.course} , {self.rating}'


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='favorite_user')
    favorite_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f' {self.user}'


class CarCourse(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # quantity = models.PositiveSmallIntegerField(default=1)

# covered_skills=models.TextField()
#    # Камтылган көндүмдөр,Охватываемые навыки::
