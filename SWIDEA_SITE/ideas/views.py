# ideas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, IdeaStar, DevTool  # DevTool 모델 포함됐다고 가정
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Count
from .forms import DevToolForm
from .forms import IdeaForm

# ✅ 아이디어 리스트
def idea_list(request):
    sort = request.GET.get('sort', 'latest')
    ideas = Idea.objects.all()

    if sort == 'likes':
        ideas = ideas.annotate(like_count=Count('stars')).order_by('-like_count', '-created_at')
    elif sort == 'title':
        ideas = ideas.order_by('title')
    elif sort == 'created':
        ideas = ideas.order_by('id')
    else:  # 최신순
        ideas = ideas.order_by('-created_at')

    if request.user.is_authenticated:
        idea_ids = [idea.id for idea in ideas]
        starred_ids = set(IdeaStar.objects.filter(user=request.user, idea_id__in=idea_ids).values_list('idea_id', flat=True))
        for idea in ideas:
            idea.starred = idea.id in starred_ids
    else:
        for idea in ideas:
            idea.starred = False

    return render(request, 'ideas/idea_list.html', {'ideas': ideas})

# ✅ 아이디어 상세
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    starred = False
    if request.user.is_authenticated:
        starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()
    return render(request, 'ideas/idea_detail.html', {'idea': idea, 'starred': starred})

# ✅ 아이디어 생성
def idea_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        dev_tool_id = request.POST.get('dev_tool')  # get() 사용하면 에러 안남
        image = request.FILES.get('image')

        dev_tool = DevTool.objects.get(pk=dev_tool_id) if dev_tool_id else None

        idea = Idea.objects.create(
            title=title,
            content=content,
            dev_tool=dev_tool,
            image=image
        )
        return redirect('idea_detail', pk=idea.pk)

    devtools = DevTool.objects.all()
    return render(request, 'ideas/idea_form.html', {'devtools': devtools})

# ✅ 아이디어 수정
def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.title = request.POST.get('title')
        idea.content = request.POST.get('content')
        dev_tool_id = request.POST.get('dev_tool')
        if dev_tool_id:
            idea.dev_tool = DevTool.objects.get(pk=dev_tool_id)
        if request.FILES.get('image'):
            idea.image = request.FILES['image']
        idea.save()
        return redirect('idea_detail', pk=pk)

    # 여기 중요: devtools를 넘겨줘야 select에 보임
    devtools = DevTool.objects.all()
    return render(request, 'ideas/idea_form.html', {
        'idea': idea,
        'devtools': devtools
    })
# ✅ 아이디어 삭제
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('idea_list')

# ✅ 찜 기능
@login_required
def toggle_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    star, created = IdeaStar.objects.get_or_create(user=request.user, idea=idea)
    if not created:
        star.delete()
        return JsonResponse({'starred': False})
    return JsonResponse({'starred': True})

# ✅ 관심도 조절
@require_POST
def adjust_interest(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    action = request.POST.get('action')

    if action == 'up':
        idea.interest += 1
    elif action == 'down' and idea.interest > 0:
        idea.interest -= 1
    idea.save()

    return JsonResponse({'interest': idea.interest})

# ✅ 개발툴 등록
def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devtool_list')
    else:
        form = DevToolForm()
    return render(request, 'ideas/devtool_form.html', {'form': form})

# ✅ 개발툴 리스트
def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'ideas/devtool_list.html', {'devtools': devtools})

# ✅ 개발툴 상세
def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    ideas = Idea.objects.filter(dev_tool=devtool)  # 연결된 아이디어들
    return render(request, 'ideas/devtool_detail.html', {
        'devtool': devtool,
        'ideas': ideas  # 넘겨줌
    })


def devtool_edit(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtool_detail', pk=pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'ideas/devtool_form.html', {
        'form': form,
        'is_edit': True  # 템플릿에서 수정 모드 구분 가능
    })

def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    devtool.delete()
    return redirect('devtool_list')