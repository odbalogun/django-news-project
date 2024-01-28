from django.db import models
from django.conf import settings
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255) #type: ignore
    body = models.TextField() #type: ignore
    date = models.DateTimeField(auto_now_add=True) #type: ignore
    author = models.ForeignKey( #type: ignore
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # new

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments") #type: ignore
    comment = models.CharField(max_length=140) #type: ignore
    author = models.ForeignKey( #type: ignore
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("article_list")