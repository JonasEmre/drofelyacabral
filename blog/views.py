from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog-ana-sayfa.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/blog.html', {'blog': blog})
