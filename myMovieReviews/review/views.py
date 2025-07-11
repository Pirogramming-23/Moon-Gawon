from django.shortcuts import render,redirect
from .models import Review
from django.shortcuts import get_object_or_404

def review_list(request, *args, **kwagrs) :
    review = Review.objects.all()
    context = {
    "review" : review
}
    return render(request, "review_list.html", context)

def review_read(request, pk):  
    reviews = Review.objects.get(id=pk)
    context = {
    "reviews" : reviews
}
    return render(request, "review_read.html", context)

def review_create(request):
    if request.method == "POST":
        rating = request.POST.get("rating")
        rating = float(rating) if rating else 0.0  # 빈값이면 0.0 처리

        Review.objects.create(
            title=request.POST["title"],
            user=request.POST["user"],
            actor=request.POST["actor"],
            genre=request.POST["genre"],
            rating=rating,
            running_time=request.POST.get("running_time", 0),
            content=request.POST["content"],
            year=request.POST.get("year", 2000),
            img=request.FILES.get("img")
        )
        return redirect("review_list")

    return render(request, "review_form.html", {
        "review": None,
        "form_action": "/review/create/",
        "is_update": False
    })

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        review.title = request.POST["title"]
        review.year=request.POST["year"]
        review.user = request.POST["user"]
        review.actor = request.POST["actor"]
        review.genre = request.POST["genre"]
        review.rating = float(request.POST.get("rating", 0))
        review.running_time = int(request.POST.get("running_time", 0))
        review.content = request.POST["content"]
        review.year = int(request.POST.get("year", 2000))

        # 이미지가 새로 업로드됐을 경우만 덮어쓰기
        if request.FILES.get("img"):
            review.img = request.FILES["img"]

        review.save()
        return redirect("review_read", pk=review.id)

    return render(request, "review_form.html", {
        "review": review,
        "form_action": f"/review/{pk}/update/",
        "is_update": True
    })

def review_delete(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('review_list')

