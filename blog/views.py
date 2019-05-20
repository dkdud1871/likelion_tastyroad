from django.shortcuts import render, get_object_or_404, redirect
from .models import Tastyroad, Comment
from django.utils import timezone
from .forms import TastyroadForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
 
    tastyroads=Tastyroad.objects
    return render(request, 'blog/home.html', {'tastyroads':tastyroads})
def detail(request, tastyroad_id):
    tastyroad_detail = get_object_or_404(Tastyroad, pk=tastyroad_id)
    form=CommentForm()
    return render(request, 'blog/detail.html',{'tastyroad':tastyroad_detail, 'form':form,})    
@login_required
def tastyroad_new(request):
    if request.method =="POST":
        form = TastyroadForm(request.POST)
        if form.is_valid():
            tastyroad =form.save(commit=False)
            tastyroad.published_date= timezone.datetime.now()
            tastyroad.save()
            return redirect('detail', tastyroad_id=tastyroad.pk)
    else:
        form= TastyroadForm()
    return render(request, 'blog/tastyroad_new.html',{'form':form})        

def tastyroad_edit(request, tastyroad_id):
    tastyroad=get_object_or_404(Tastyroad, pk=tastyroad_id)
    if request.method =="POST":
        form= TastyroadForm(request. POST , instance=tastyroad)
        if form.is_valid():
            tastyroad=form.save(commit=False)
            tastyroad.published_date =timezone.datetime.now()
            tastyroad.save()
            return redirect('detail', tastyroad_id=tastyroad.pk)
    else:
        form =TastyroadForm(instance=tastyroad)
    return render(request, 'blog/tastyroad_edit.html',{'form':form})   

def tastyroad_delete(request, tastyroad_id):
    tastyroad =get_object_or_404(Tastyroad, pk=tastyroad_id)
    tastyroad.delete()
    return redirect('home')

def add_comment(request, tastyroad_id):
    tastyroad=get_object_or_404(Tastyroad, pk=tastyroad_id)
    if request.method =="POST":
        form= CommentForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.tastyroad=tastyroad
            comment.save()
    return redirect('detail', tastyroad_id=tastyroad.pk)        

def comment_delete(request, comment_id):
    comment =get_object_or_404(Comment, pk=comment_id)
    tastyroad=comment.tastyroad
    comment.delete()
    return redirect('detail' , tastyroad_id=tastyroad.id)