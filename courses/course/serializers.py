from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# lay access_token: /o/token/
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data, **kwargs):
        # **validated_data : chuyen toan bo k can chuyen tung fields
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        return user


# chuyen queryset thanh data
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class LessonSerializer(ModelSerializer):
    # the hien tag o trong lesson
    # many = True: do co nhieu field trong model
    tags = TagSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'content', 'create_date', 'course', 'image', 'tags', 'active']
