from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
# Create your views here.

def index(request):
    entries = Entry.objects.order_by('-date_posted')
    ##Entry.objects.all().delete()  ## UnComment it to flash the database
    context = {'entries' : entries}
    return render(request,'entries/index.html',context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('index')
    else:
        form = EntryForm()
    context = { 'form' : form }
    return render(request,'entries/add.html',context)

def reset(request):
    Entry.objects.all().delete()
    entries = Entry.objects.order_by('-date_posted')
    context = { 'entries' : entries}
    return render(request,'entries/index.html',context)