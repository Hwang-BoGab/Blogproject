from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내는것
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'home.html', {'blogs' : blogs, 'posts':post})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blogs =Blog()
    blogs.title = request.GET['title']
    blogs.body = request.GET['body']
    blogs.pub_date = timezone.datetime.now()
    blogs.save()
    return redirect('/blog/'+str(blogs.id)) 

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    #2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})




