from django.db import models

class Post(models.Model):
    #user_id =
    #file_url =

    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'[{self.pk}]{self.title}'

# class Bookmark(models.Model):
#     title = models.CharField(max_length=200)
#     url = models.URLField(verbose_name='Site URL')