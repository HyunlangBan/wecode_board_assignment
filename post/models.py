from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=40)
    password = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f'{self.author} {self.title}'
