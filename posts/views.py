from urllib.parse import quote
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.utils import timezone
from django.db.models import Q

from . models import Post
from . forms import PostForm


# Create your views here.
def post_create(request): #create post
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user  = request.user
        instance.save()
        messages.success(request, "post successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form':form,
    }
    return render(request, 'posts/post_form.html', context)

def post_detail(request, slug ): #retrieve post
    instance = get_object_or_404(Post, slug=slug )
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    quote_tag = quote(instance.content)
    context  = {
        'title':instance.title,
        'instance':instance,
        "quote_tag":quote_tag,
    }
    return render(request,'posts/post_detail.html', context)

def post_list(request): #list all post
    instance_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        instance_list = Post.objects.all()
    query  = request.GET.get("q")
    if query:
        instance_list = instance_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)).distinct()
    
    page_request_var = "page"        
    paginator = Paginator(instance_list, 5, orphans=3)

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
        'title': 'Latest post',
        'page_request_var':page_request_var
    }
    return render(request, 'posts\post_list.html', context)


def post_update(request, slug=None ): #edit post
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "succesfully deleted")
    return redirect("posts/post_list")
