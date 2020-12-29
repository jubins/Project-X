from django.shortcuts import render, redirect
from . forms import SignupForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
