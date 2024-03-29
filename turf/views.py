from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from turf.models import tbl_turf
from django.db import models

# Create your views here.

def turfowner(request):
    data = tbl_turf.objects.all()
    return render(request,"turfowner1.html", {'data1':data})

def addturf(request):
    return render(request,"addturf1.html")  

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
    return render(request,"addturf1.html")

def viewturf(request):
    data = tbl_turf.objects.all()
    return render(request,"viewturf.html", {'data1':data})

def removeturf(request,id):
    data = tbl_turf.objects.get(id=id)
    data.delete()
    return redirect('/viewturf')

def edit_turf(request,id):
    data = tbl_turf.objects.get(id=id)
    return render(request,"edit_turf.html",{'data1':data})

def update_turf(request,id):
    data = tbl_turf.objects.get(id=id)
    data.turf_name = request.POST.get('turfname')
    data.contact_no = request.POST.get('contactnumber')
    data.email = request.POST.get('email')
    data.working_hrs = request.POST.get('workinghours')
    data.fee = request.POST.get('fee')


    data.save()
    return redirect('/viewturf')