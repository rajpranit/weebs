from django.db import models
from django.contrib.auth.models import User


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

# class genre(models.Model):
#     manhwa = models.ForeignKey(manhwa,null=True, blank=True,on_delete=models.CASCADE)
#     manhua = models.ForeignKey(manhua,null=True, blank=True,on_delete=models.CASCADE)
#     anime = models.ForeignKey(anime,null=True, blank=True,on_delete=models.CASCADE)
#     doujins = models.ForeignKey(doujins,null=True, blank=True,on_delete=models.CASCADE)
#     hentai = models.ForeignKey(hentai,null=True, blank=True,on_delete=models.CASCADE)

#     def __str__(self):
#         if manhwa:
#             return f"manhwa"
#         if manhua:
#             return f"manhua"
#         if anime:
#             return f"anime"
#         if doujins:
#             return f"doujins"
#         if hentai:
#             return f"hentai"

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    manhwa = models.ManyToManyField(manhwa,blank=True,null=True)
    manhua = models.ManyToManyField(manhua,blank=True)
   
    created_on = models.DateTimeField(null=True)
    Type = models.CharField(max_length=45,null=True,blank=True)
   

    def __str__(self):
        return f"{self.title} | {self.author}"
