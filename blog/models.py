from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')    #при удалении юзера удалятся все посты связанные с ним
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    tags = TaggableManager()

    class Meta:
        ordering = ("-created_at", ) #новые в начале

    def get_absolute_url(self):
        return reverse("post_single", args=[self.slug])

    def __str__(self) -> str:
        return self.title


    

