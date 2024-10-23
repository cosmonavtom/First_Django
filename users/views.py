from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from users.models import User
from users.forms import UserRegisterForm


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('dogs:index'))
    return render(request, 'users/register_user.html', {'form': UserRegisterForm}, )
