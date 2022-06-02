from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import null


class manhwa(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    author = models.CharField(max_length=225,null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    story = models.TextField()
    chapters = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return f"{self.title} | {self.chapters}"

class manhua(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225,null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    story = models.TextField()
    chapters = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return f"{self.title} | {self.chapters}"

class anime(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225,null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    story = models.TextField()
    episodes = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return f"{self.title} | {self.episodes}"

class doujins(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225,null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    story = models.TextField()
    chapters = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return f"{self.title} | {self.chapters}"

class hentai(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225,null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    story = models.TextField()
    chapters = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return f"{self.title} | {self.chapters}"


class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    manhwa = models.ManyToManyField(manhwa,blank=True)
    manhua = models.ManyToManyField(manhua,blank=True)
    poster_image_lg = models.ImageField(blank=True,null=True,upload_to='images/')
    poster_image = models.ImageField(blank=True,null=True,upload_to='images/Poster')
    poster_image_md = models.ImageField(blank=True,null=True,upload_to='images/')
    poster_image_sm = models.ImageField(blank=True,null=True,upload_to='images/')
    created_on = models.DateTimeField(null=True)
    Type = models.CharField(max_length=45,null=True,blank=True)
   

    def __str__(self):
        return f"{self.title} | {self.author}"

class ManhwaPost(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    manhwa = models.ManyToManyField(manhwa,blank=True)
    manhua = models.ManyToManyField(manhua,blank=True)
    poster_image_lg = models.ImageField(blank=True,null=True,upload_to='images/')
    poster_image = models.ImageField(blank=True,null=True,upload_to='images/Poster')
    poster_image_md = models.ImageField(blank=True,null=True,upload_to='images/')
    poster_image_sm = models.ImageField(blank=True,null=True,upload_to='images/')
    created_on = models.DateTimeField(null=True)
    Type = models.CharField(max_length=45,null=True,blank=True)
   

    def __str__(self):
        return f"{self.title} | {self.author}"
