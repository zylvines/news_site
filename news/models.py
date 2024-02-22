from django.db import models


class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    TAGS = (
        ('Yangi', 'Yangi'),
        ('Dolzarb', 'Dolzarb'),
        ('Qaynoq', 'Qaynoq'),
    )

    slug = models.SlugField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    tags = models.CharField(max_length=150, choices=TAGS, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

