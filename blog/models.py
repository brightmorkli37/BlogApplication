from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Blog(models.Model):

    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=105)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    # body = models.TextField()
    body = RichTextField()
    date_published = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE, max_length=50)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:60]

    class Meta:
        ordering = ('-date_published',)