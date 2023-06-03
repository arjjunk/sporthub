from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from turf.models import tbl_turf
from django.db import models

# Create your views here.

def turfowner(request):
    return render(request,"turfowner.html")

def addturf (request):
    return render(request,"addturf.html")  

def turfadd(request):
    if request.method == 'POST':
        data = tbl_turf()
        data.turf_id = "na"
        data.turf_name = request.POST.get('turfname')
        data.contact_no = request.POST.get('contactnumber')
        data.email = request.POST.get('email')
        data.working_hrs = request.POST.get('workinghours')
        data.location = request.POST.get('location')
        data.fee = request.POST.get('fee')
        Photo = request.FILES['photos']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name,Photo)
        uploaded_file_url = fs.url(filename)
        data.photo = uploaded_file_url
        data.save()
        data.status = "open"
        data.save()
        data.turf_id = "TF"+str(data.id)
        data.save()
    return render(request,"addturf.html")

def viewturf(request):
    data = tbl_turf.objects.all()
    return render(request,"viewturf.html", {'data1':data})