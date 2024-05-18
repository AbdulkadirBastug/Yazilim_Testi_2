from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth,messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from myproject.models import BlogPost , Industry

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request,'index.html',{'username' : username})
    else:
        return redirect('/login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request,'login.html',{'Error' : True})
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('register')

        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return render(request,'register.html')
    else:
        return render(request,'register.html')
    
def blog(request):
    if not request.user.is_authenticated:
        return redirect('/login')                                
    user_posts = BlogPost.objects.filter(author=request.user)  
    return render(request, 'blog.html', {'blog_posts': user_posts})

def industry(request):
    if not request.user.is_authenticated:
        return redirect('/login')                                
    industry = Industry.objects.filter(author=request.user) 
    return render(request, 'industry.html', {'industry': industry})

def singleBlog(request,post_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'singleBlog.html', {'post': post})

def singleIndustry(request,post_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    post = get_object_or_404(Industry, id=post_id)
    return render(request, 'singleIndustry.html', {'post': post})


def blogSave(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            image = request.FILES.get('image')  
            

            if BlogPost.objects.filter(title=title).exists():
                messages.error(request, "Title is already exists.")
                return redirect('blogSave')
            
            blog_post = BlogPost(title=title, content=content, author=request.user, image=image)
            blog_post.save()

            messages.success(request, 'Blog post saved successfully!')

            return render(request, 'blogSave.html')  
        else:
            return render(request, 'blogSave.html')
    else:
        return redirect('/login')


def industrySave(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            content = request.POST.get('content')
            image = request.FILES.get('image')  


            if Industry.objects.filter(name=name).exists():
                messages.error(request, "Industry is already exists.")
                return redirect('industrySave')

            industry = Industry(name=name, content=content, author=request.user, image=image)
            industry.save()

            messages.success(request, 'Industry saved successfully!')

            return render(request, 'industrySave.html')
        else:
            return render(request, 'industrySave.html')
    else:
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/login')