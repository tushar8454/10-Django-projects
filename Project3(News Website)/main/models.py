from django.db import models

# Create your models here.

class Author(models.Model):
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.author
    
class Categories(models.Model):
        name=models.CharField(max_length=100)
        def __str__(self):
             return self.category   


class News(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    categories=models.ManyToManyField('Categories')
    title=models.CharField(max_length=400)
    discription=models.CharField(max_length=800)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
