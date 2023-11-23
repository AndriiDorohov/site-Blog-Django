import os
import pytz

from PIL import Image

from django.contrib.auth.models import User
from django.contrib.auth import get_user, get_user_model
from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.utils import timezone


def image_filename(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = f"{instance.title}.{ext}"
    return os.path.join("images", new_filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)
    twitter_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        if not self.pk and not self.image:
            self.image.save(
                'default.jpg',
                ContentFile(settings.DEFAULT_PROFILE_PIC.read()),
                save=False,
            )

        super(Profile, self).save(*args, **kwargs)

  #  def save(self, *args, **kwargs):
  #       super(Profile, self).save(*args, **kwargs)

  #       img = Image.open(self.image.path)
  #       if img.height > 300 or img.width > 300:
  #           output_size = (300, 300)
  #           img.thumbnail(output_size)
  #           img.save(self.image.path)

    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path) # Open image

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.image.path) # Save it again and override the larger image

    @property
    def published_posts_count(self):
        return self.user.article_set.filter(status='published').count()

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    author_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    full_text = models.TextField()
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255, unique=True)
    og_image = models.ImageField(upload_to=image_filename, null=True)
    # is_published = models.BooleanField() #TODO
    likes = models.ManyToManyField(User, related_name="liked_articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_page", kwargs={"slug": self.slug})

    def get_category_url(self):
        return reverse("category_page", kwargs={"category": self.category})

    def get_author_url(self):
        return reverse("author_page", kwargs={"author_name": self.author_name})

    def author_profile(self):
        return Profile.objects.get(user=self.author)

    def save(self, *args, **kwargs):
        user_timezone = pytz.timezone("Europe/Kiev")
        if self.pubdate is None:
            now = timezone.now()
            localized_time = now.astimezone(user_timezone)
            self.pubdate = localized_time

        super().save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
