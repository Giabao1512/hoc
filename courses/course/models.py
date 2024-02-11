from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


# lay current user = request.user
# rang buoc login cho def: @login_required
# class: ke thua LoginRequiredMixin
class User(AbstractUser):
    avatar = CloudinaryField('avatar', null=False)


class ItemBase(models.Model):
    class Meta:
        abstract = True

    subject = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    # Lesson.objects.filter(create_date__month__range = [7, 10]) -> vùng
    # Lesson.objects.filter(create_date__month__in = [7, 10]) -> trong từng thánng
    # gt -> lớn hơn, gte -> lớn or =, lt -> bé hơn, lte -> bé or =
    # iregex = '(giai thuat | thuat giai)'
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)


# many to many
class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')

    content = RichTextField(default=None)
    # relate_name để thay thế: c.lesson_get.all() => c.lessons.all()
    # truy van: Course.objects.filter(lessons__active = True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="lessons")
    tags = models.ManyToManyField('Tag', blank=True, null=True, related_name="lessons")
    image = models.ImageField(upload_to='lessons/%Y/%m', default=None)

    def __str__(self):
        return self.subject


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


category_info = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)


# many to one
class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')

    # truy van: Course.objects.filter(category__name__contains = "..")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)

    def __str__(self):
        return self.subject


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
