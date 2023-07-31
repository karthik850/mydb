from django.db import models
from pyexpat import model

# Create your models here.

class MyYotubeVideos(models.Model):
    videoName = models.CharField(max_length=1000)
    thumbnail=models.URLField(default="https://drive.google.com/uc?export=view&id=143yjY3rCG_R4EWR61iOAb-XynE1ZRUFl")
    description=models.TextField()
    url=models.CharField(max_length=5000,null=True,default="default")
    
    def __str__(self):
        return self.videoName

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'MyYotubeVideo'
        verbose_name_plural = 'MyYotubeVideos'

class SubscriberStories(models.Model):
    storyTitle = models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    story=models.TextField()
    
    def __str__(self):
        return self.storyTitle

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'SubscriberStorie'
        verbose_name_plural = 'SubscriberStories'

class YoutubeEvents(models.Model):
    eventName = models.CharField(max_length=1000)
    eventDate=models.CharField(max_length=1000)
    eventDescription=models.TextField()
    eventImage=models.URLField(blank=True)
    
    def __str__(self):
        return self.eventName

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'YoutubeEvent'
        verbose_name_plural = 'YoutubeEvents'

class MileStones(models.Model):
    milestoneName = models.CharField(max_length=1000)
    mileStoneDate=models.DateField()
    
    def __str__(self):
        return self.milestoneName

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'MileStone'
        verbose_name_plural = 'MileStones'

