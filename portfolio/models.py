from pyexpat import model
from django.db import models

# Create your models here.

class Projects(models.Model):
    projectName = models.CharField(max_length=1000)
    technology = models.CharField(max_length=2000)
    projectImage=models.URLField(default="https://shit.management/content/images/size/w2000/2019/07/team_work.jpg")
    description=models.TextField()
    url=models.CharField(max_length=5000,null=True,default="default")
    video=models.CharField(max_length=5000,null=True,default="default")
    
    def __str__(self):
        return self.projectName

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Project'
        verbose_name_plural = 'Project'
