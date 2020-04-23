from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Category(models.Model):
    catName = models.CharField(max_length=300)


class Post(models.Model):
    title = models.CharField(max_length=350)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    is_published = models.BooleanField(default='false')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Main(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CurrentUserDefault(object):
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)