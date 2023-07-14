# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from datetime import datetime, timedelta
# from .models import IQQuestion, UserIQResponse

# @login_required
# def iq_test(request):
#     questions = IQQuestion.objects.all()
#     time_limit = 10  # Specify the time limit in minutes

#     if request.method == 'POST':
#         start_time_str = request.session.get('start_time')
#         if not start_time_str:
#             return redirect('iq_test')

#         start_time = datetime.fromisoformat(start_time_str)
#         end_time = datetime.now()
#         elapsed_time = end_time - start_time

#         if elapsed_time.total_seconds() > time_limit * 60:
#             # Time limit exceeded
#             for question in questions:
#                 user_answer = request.POST.get(str(question.id))
#                 UserIQResponse.objects.create(user=request.user, question=question, response=user_answer)

#             messages.warning(request, 'Time limit exceeded. Your answers have been automatically submitted.')
#             return redirect('iq_test_results')

#         score = 0
#         for question in questions:
#             user_answer = request.POST.get(str(question.id))
#             if user_answer and user_answer.lower() == question.answer.lower():
#                 score += 1
#             UserIQResponse.objects.create(user=request.user, question=question, response=user_answer)

#         messages.success(request, f'Your IQ test score is {score}')
#         return redirect('score')
#     else:
#         request.session['start_time'] = datetime.now().isoformat()

#     context = {
#         'questions': questions,
#         'time_limit': time_limit,
#     }
#     return render(request, 'Iq_Test/iqtest.html', context)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime, timedelta
from .models import IQQuestion, UserIQResponse,UserScore
from Departments.models import Departments,News,FAQ,Location_Info,About_Us,Students,Courses

@login_required(login_url='login')
def iq_test(request):
    questions = IQQuestion.objects.all()
    time_limit = 10  # Specify the time limit in minutes

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    if request.method == 'POST':
        start_time_str = request.session.get('start_time')
        if not start_time_str:
            return redirect('iq_test')

        start_time = datetime.fromisoformat(start_time_str)
        end_time = datetime.now()
        elapsed_time = end_time - start_time

        if elapsed_time.total_seconds() > time_limit * 60:
            # Time limit exceeded
            for question in questions:
                user_answer = request.POST.get(str(question.id))
                UserIQResponse.objects.create(user=request.user, question=question, response=user_answer)

            messages.warning(request, 'Time limit exceeded. Your answers have been automatically submitted.')
            return redirect('iq_test_results')

        score = 0
        for question in questions:
            user_answer = request.POST.get(str(question.id))
            if user_answer and user_answer.lower() == question.answer.lower():
                score += 1
            UserIQResponse.objects.create(user=request.user, question=question, response=user_answer)

        user_score, created = UserScore.objects.get_or_create(user=request.user)
        user_score.score = score
        user_score.save()

        messages.success(request, f'Your IQ test score is {score}')
        return redirect('score')
    else:
        request.session['start_time'] = datetime.now().isoformat()

    context = {
        'questions': questions,
        'time_limit': time_limit,
        'departments':departments,
        'news':news,
        'faq':faq,
        'location':location,
    }
    return render(request, 'Iq_Test/iqtest.html', context)


@login_required(login_url='login')
def iq_test_results(request):
    user_responses = UserIQResponse.objects.filter(user=request.user)

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    context = {
        'user_responses': user_responses,
        'departments':departments,
        'news':news,
        'faq':faq,
        'location':location,
    }
    return render(request, 'Iq_Test/score.html', context)
