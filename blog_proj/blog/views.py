from django.shortcuts import render,redirect, get_object_or_404
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required



@login_required
def PostView(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form  = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('postview')


    else :
        form = PostModelForm()

    context = {'posts' : posts,'form' : form}
    
    return render(request, 'blog/index.html',context)


@login_required
def post_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    comments = post.commentmodel_set.all()
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('postdetail', pk = post.id)

    else :
        c_form = CommentForm()
    context ={
'post' : post,
'comment' : comments,
'c_form' : c_form
    }
    return render(request,'blog/post_detail.html',context)

@login_required
def post_edit(request,pk):
    post = get_object_or_404(PostModel, pk=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('postdetail', pk=post.id)
    else : 
        form = PostUpdateForm(instance = post)
                
    context = {
'post' : post,
'form' : form,
    }
    return render(request,"blog/post_edit.html",context)

@login_required
def post_delete(request,pk):
    post = get_object_or_404(PostModel,pk = pk)
    if request.method == 'POST':
        post.delete()
        return redirect('postview')

    context = {
        'post' : post
    }
    return render(request,'blog/post_delete.html', context)