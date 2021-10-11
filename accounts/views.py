from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts/login.html')
#     else:
#         form = UserCreationForm()
#     form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})
#
#
# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             return redirect('/')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})





from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # phone = request.POST['phone']
        password = request.POST['password']
        # psw2 = request.POST['psw2']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/accounts/login')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username: request.POST['username']
        password: request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("")
        else:
            return redirect('/upload/filo/')

    else:
        return render(request, 'login.html')

