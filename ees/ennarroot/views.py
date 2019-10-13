from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,Http404
from django.shortcuts import reverse
from django.core.files.storage import FileSystemStorage
from ennarroot.models import Admin_list,Products


def index(request):
    return render(request,'ennarroot.html',context=None)


def admin(request):
    return render(request,'admin.login/login.html',context=None)


def adminLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        passcode=request.POST['passcode']
        try:
            user=Admin_list.objects.get(user_name=username,passcode=passcode)

        except Exception as ex:
            print('error')
            return HttpResponse('<script> alert("login failed!!!   check for username or password")</script>')
        request.session['user']=username
        return HttpResponseRedirect(reverse('ennarroot:admin_desk'))



def adminDesk(request):
    username = request.session.get('user')
    username=toUpper(username)

    return render(request,'Admin/Admin.html',context={'username':username})

def logout(request):
    del request.session['user']
    request.session.modified = True
    return HttpResponseRedirect(reverse('ennarroot:home'))

def productUpload(request):
    if request.method=='POST':
        product_name=request.POST['product_name']
        capacity=request.POST['capacity']
        pressure=request.POST['working_pressure']
        fuel=request.POST['fuel']
        model=request.POST['model_series']
        file=request.FILES['image']
        file_storage=FileSystemStorage()
        name=file_storage.save(file.name,file)
        file_url=file_storage.url(name)
        product=Products(productname=product_name,capacity=capacity,workingpressure=pressure,fuel=fuel,model_series=model,product_image=file_url)
        try:

            product.save()
        except Exception as ex:
            print(ex)
            return HttpResponse('<script> alert("something went wrong ")</script>')

        return HttpResponseRedirect(reverse('ennarroot:home'))

def uploadForm(request):
    return render(request,'productupload.html',context=None)

def toUpper(name):
     index=0
     for a in iter(name):
             if index==0:
                     resname=a.upper()
                     index+=1
             else:
                    resname+=a
                    index+=1
     return resname