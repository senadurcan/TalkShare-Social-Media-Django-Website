from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(("Category Name"), max_length=100,null=True , blank=True)
    
    def __str__(self) -> str:
        return self.title



class Social(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True , blank=True)
    title = models.CharField(("Başlık"),max_length=100)
    text = models.TextField(("Yazı"))
    date_now = models.DateTimeField(("Tarih"), auto_now_add=True)
    like = models.IntegerField(("Beğen"),null=True , blank=True)
    
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    social = models.ForeignKey(Social, verbose_name=("Social"), on_delete=models.CASCADE,null=True , blank=True)
    name = models.CharField(("Name Surname"), max_length=100)
    comment = models.TextField(("Comment"))
    date_now = models.DateTimeField(("Tarih"), auto_now_add=True,null=True , blank=True)
    
    def __str__(self) -> str:
        return self.social