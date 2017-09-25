from urllib.parse import quote
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect


from . models import Post
from . forms import PostForm
# Create your views here.
def post_create(request): #create post
    form = PostForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "post successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form':form,
    }
    return render(request, 'posts/post_form.html', context)

def post_detail(request, slug ): #retrieve post
    instance = get_object_or_404(Post, slug=slug )
    quote_tag = quote(instance.content)
    context  = {
        'title':instance.title,
        'instance':instance,
        "quote_tag":quote_tag,
    }
    return render(request,'posts/post_detail.html', context)

def post_list(request): #list all post
    instance_list = Post.objects.all()
    paginator = Paginator(instance_list, 10, orphans=5)
    page_request_var = "page"

    page = request.GET.get(page_request_var)
    try:
        instance = paginator.page(page)
    except PageNotAnInteger:
		# If page is not an integer, deliver first page.
        instance = paginator.page(1)
    except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
        instance = paginator.page(paginator.num_pages)

    context  = {
        'instance':instance,
        'title': 'List',
        'page_request_var':page_request_var
    }
    return render(request, 'posts\post_list.html', context)

def post_update(request, slug=None ): #edit post
    instance = get_object_or_404(Post, slug=slug )
    form     = PostForm(request.POST or None,request.FILES or None , instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>post saved</a>", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context  = {
        'title':instance.title,
        'instance':instance,
        'form':form,
    }    
    return render(request, 'posts/post_form.html', context)


def post_delete(request, slug): #delete post
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "succesfully deleted")
    return redirect("posts:post_list")
