from django.db import models

class Blogs(models.Model):
    topic= models.CharField(blank=False, max_length=250,default="")
    content=models.TextField(max_length=1000,default="")
    image_url=models.CharField(blank=True,max_length=1000,default="")
    posted_date_time=models.CharField(blank=False,max_length=250,default="")
    posted_date=models.CharField(blank=False,max_length=250,default="")
    posted_month=models.CharField(blank=False,max_length=250,default="")
    posted_year=models.CharField(blank=False,max_length=250,default="")

    def __str__(self):
        return(self.topic)
