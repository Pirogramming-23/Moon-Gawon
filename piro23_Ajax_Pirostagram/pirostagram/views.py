from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'pirostagram/pirostagram.html', {'posts': posts})

@login_required
def like_ajax(request):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        "result": "ok",
        "like_count": post.likes.count(),
        "liked": liked,
    })

@login_required
def comment_create_ajax(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        content = request.POST.get("content")
        post = get_object_or_404(Post, id=post_id)

        comment = Comment.objects.create(user=request.user, post=post, content=content)
        return JsonResponse({
            "id": comment.id,
            "user": comment.user.username,
            "content": comment.content
        })


@login_required
def comment_delete_ajax(request):
    comment_id = request.POST.get("comment_id")
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.delete()
    return JsonResponse({'success': True})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all().order_by('-id')  # ← related_name="comments"
    return render(request, 'pirostagram/post_detail.html', {
        'post': post,
        'comments': comments,
    })
