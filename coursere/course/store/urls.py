from django.urls import path,include
from .views import *
from rest_framework import routers
router=routers.SimpleRouter()


router.register(r'online',Online_Examination_SystemViewSet,basename='online_list')
router.register(r'user',UserProfileViewSet,basename='user_list')
router.register(r'questions',QuestionsViewSet,basename='questions_list')
router.register(r'courses',CoursesViewSet,basename='courses_list')
router.register(r'course',CourseViewSet,basename='course_list')
router.register(r'lesson',LessonViewSet,basename='lesson_list')
router.register(r'course_video',CourseVideoViewSet,basename='course_video_list')
router.register(r'lesson_video',LessonVideoViewSet,basename='lesson_video_list')
router.register(r'assignment',AssignmentViewSet,basename='assignment_list')
router.register(r'',ExamViewSet,basename='exam_list')
router.register(r'certificate',CertificateViewSet,basename='certificate_list')
router.register(r'favorite',FavoriteViewSet,basename='favorite_list')
router.register(r'cart',CartViewSet,basename='cart_list')
router.register(r'carcourse',CarCourseViewSet,basename='carcourse_list')

urlpatterns=[
    path('',include(router.urls)),
]