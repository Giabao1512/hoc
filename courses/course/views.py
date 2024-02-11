from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from django.views import View
from rest_framework import viewsets, permissions, status, generics
from .serializers import *
from rest_framework.parsers import MultiPartParser


# def index(request):
#     return render(request,'home.html', context={'name' : 'Gia bao dep trai'})
#
#
# def course_detail(request, course_id):
#     try:
#
#         course = Course.objects.get(pk=course_id)
#
#     except Course.DoesNotExits:
#
#         return HttpResponseNotFound("<h1>Khong tim thay</h1>")
#
#     return render(request,'courses/course_detail.html', {'course': course})
#
#
# class CourseView(View):
#     def get(self, request):
#         return HttpResponse("welcome")
#
#     def post(self, request):
#         pass


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    # phan quyen
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]


class LessonView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    # an 1 lesson
    @action(methods=['POST'], detail=True, url_path='hide_lesson')
    # lesson/{pk}/hide_lesson
    def HideLesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=LessonSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)

    # def get_permissions(self):
    # muon add_comment voi like thi phai chung thuc
    #     if self.action in ['add_comment', 'like']:
    #         return [permissions.IsAuthenticated()]
    #
    #     return self.permission_classes
    #
    # @action(methods=['post'], url_path='comments', detail=True)
    # def add_comment(self, request, pk):
    #     c = Comment.objects.create(user=request.user, lesson=self.get_object(), content=request.data.get('content'))
    #
    #     return Response(serializers.CommentSerializer(c).data, status=status.HTTP_201_CREATED)


# viewsets.ViewSet k co san nhu ModelViewSet
class UserView(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer