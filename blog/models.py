from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=200, unique = True, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


