from django.urls import path, re_path, include
from . import views
from .admin import admin_site
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', views.CourseView)
router.register('lesson', views.LessonView)
router.register('users', views.UserView)
router.register('category', views.CategoryView)
# /course/ - get
# /course/ - post
# /course/{course_id}/ - get
# /course/{course_id}/ - put (cap nhat)
# /course/{course_id}/ - delete
urlpatterns = [
    # path('', views.index),
    path('admin/', admin_site.urls),
    # # bieu thuc re_path: bat dau = ^, ket thuc = $
    # re_path(r'^course/(?P<course_id>[0-9]{1,2})/$', views.course_detail),
    # path('test/', views.CourseView.as_view())
    path('', include(router.urls))
]
