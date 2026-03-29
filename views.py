from django.shortcuts import render, redirect
from .models import Question, Choice, Submission
from django.contrib.auth.models import User

# Submit function
def submit(request):
    if request.method == "POST":
        user = User.objects.first()  # simple user (for demo)

        for key, value in request.POST.items():
            if key.startswith('question_'):
                choice = Choice.objects.get(id=value)
                Submission.objects.create(
                    user=user,
                    choice=choice,
                    is_correct=choice.is_correct
                )

        return redirect('result')


# Show result function
def show_exam_result(request):
    submissions = Submission.objects.all()

    total = submissions.count()
    correct = submissions.filter(is_correct=True).count()

    score = (correct / total) * 100 if total > 0 else 0

    return render(request, 'onlinecourse/exam_result.html', {
        'total': total,
        'correct': correct,
        'score': score,
        'submissions': submissions
    })