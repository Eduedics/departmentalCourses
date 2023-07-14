from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
# from users.decorators import unauthenticated_user,allowed_users,admin_only

@login_required(login_url='login')
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after submitting the feedback
    else:
        form = FeedbackForm()

    return render(request, 'contactus/feedback.html', {'form': form})

@login_required(login_url='login')
def success(request):
    return render(request, 'contactus/success.html')
