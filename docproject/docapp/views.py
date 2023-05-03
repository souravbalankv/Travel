from django.shortcuts import render, redirect
from django.http import HttpResponse
from  . models import Document
from  .forms import DocumentForm
# Create your views here.

def index(request):
    document=Document.objects.all()
    context={
        'document_list':document
    }
    return  render(request,'index.html',context)
def detail(request,document_id):
    document=Document.objects.get(id=document_id)
    return  render(request,"detail.html",{'document':document})

def add_document(request):
    if request.method=="post":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        document=Document(name=name,desc=desc,year=year,img=img)
        document.save()

    return render(request,'add.html')

def update(request,id):
    document=Document.objects.get(id=id)
    form=DocumentForm(request.POST or None, request.FILES,instance=document)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return  render(request,'edit.html',{'form':form,'document':document})

def delete(request,id):
    if request.method=='POST':
        document=Document.objects.get(id=id)
        document.delete()
        return  redirect('/')
    return  render(request,'delete.html')