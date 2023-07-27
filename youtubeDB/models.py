from django.db import models
from pyexpat import model

# Create your models here.

class MyYotubeVideos(models.Model):
    videoName = models.CharField(max_length=1000)
    thumbnail=models.URLField(default="https://shit.management/content/images/size/w2000/2019/07/team_work.jpg")
    description=models.TextField()
    url=models.CharField(max_length=5000,null=True,default="default")
    
    def __str__(self):
        return self.videoName

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'MyYotubeVideo'
        verbose_name_plural = 'MyYotubeVideos'
