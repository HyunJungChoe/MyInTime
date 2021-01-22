from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)  # 현재시간에 맞춰서 자동 입력
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    body = RichTextUploadingField()


# Create your models here.
# class Blog(models.Model):
#     title = models.CharField(max_length=100)
#     pub_date = models.DateTimeField()
#     body = models.TextField()