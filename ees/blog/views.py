from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from blog.models import Blogs
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,Http404
from django.shortcuts import reverse
import datetime
def viweBlog(request):
    blog = Blogs.objects.all()
    return render(request,'blog.html',context={'content':blog})

def postBlog(request):

    if request.method=='POST':
        topic=request.POST['topic']
        blog=request.POST['blog']
        file=request.FILES['image']
        file_storage=FileSystemStorage()
        name=file_storage.save(file.name,file)
        file_url=file_storage.url(name)
        posted_date_time=datetime.datetime.today()
        posted_date=posted_date_time.strftime("%d")
        posted_month=posted_date_time.strftime("%b")
        posted_year=posted_date_time.strftime("%Y")
        blog =Blogs(topic=topic,content=blog,image_url=file_url,posted_date_time=posted_date_time,posted_date=posted_date,posted_month=posted_month,posted_year=posted_year)
        blog.save()
        return HttpResponseRedirect(reverse('blog:viewblog'))
    return render(request,'blogpost.html',context=None)

def deletepost(request):
    return render(request,'deletepost.html',context=None)

def deleteblog(request):
        if request.method=='POST':
            topic=request.POST['topic']
            try:
                blog=Blogs.objects.get(topic=topic)
                blog.delete()
            except Exception as e:
                return HttpResponse('<script> alert("entered topic is wrong");</script>')
        return HttpResponseRedirect(reverse('blog:viewblog'))
