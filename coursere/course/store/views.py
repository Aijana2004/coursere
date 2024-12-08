from rest_framework import viewsets
from .models import *
from .serializer import *


class Online_Examination_SystemViewSet(viewsets.ModelViewSet):
    queryset = Online_Examination_System.objects.all()
    serializer_class = Online_Examination_SystemSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonVideoViewSet(viewsets.ModelViewSet):
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideoSerializer


class CourseVideoViewSet(viewsets.ModelViewSet):
    queryset = CourseVideo.objects.all()
    serializer_class = CourseVideoSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CarCourseViewSet(viewsets.ModelViewSet):
    queryset = CarCourse.objects.all()
    serializer_class = CarCourseSerializer
