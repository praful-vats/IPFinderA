# from django.shortcuts import render
# import dns.resolver
#
#
# def index(request):
#     search = request.POST.get('search')
#
#     ip_address = dns.resolver.Resolver.resolve(search, 'A')[0]
#     # for i in ip_address:
#     context = {"ip_address": ip_address.to_text()}
#
#     return render(request, 'index.html', context)

# from django.shortcuts import render
# import ipapi
#
#
# def index(request):
#     search = request.POST.get('search')
#
#     data = ipapi.location(ip=search, output='json')
#
#     context = {"data": data}
#
#     return render(request, 'index.html', context)

# from django.shortcuts import render
# import dns.resolver
#
#
# def index(request):
#     search = request.POST.get('search')
#     my_resolver = dns.resolver.Resolver()
#     ip_address = my_resolver.resolve(search, "A")[0]
#     # ip_address = dns.resolver.Resolver.resolve(search, 'A')
#     # for i in ip_address:
#     ip = ip_address.to_text()
#     context = {"ip_address": ip}
#     return render(request, 'index.html', context)

# from django.shortcuts import render
# import dns
# import dns.resolver
# import json

# from django.shortcuts import render #, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm


# def index(request):
    # search = request.POST.get('search')

    # ip_address = dns.resolver.Resolver.resolve(search, "A")
    # ip_address = dns.resolver.query(search, "A")
    # untag

    # ip_address = dns.resolver.Resolver()
    # answers = ip_address.resolve(search, 'A').rrset[0].to_text()

    # del ip_address
    # answer=ip_address.nameservers(search=search,qname='google.com').rrset[0].to_text()
    # data = ipapi.location(ip=search, output='json')
    # try:
    #     ip_address = dns.resolver.resolve(search, 'A').rrset[0].to_text()
    # except dns.resolver.NoAnswer:
    #     ip_address = 'No answer'

    # try:
    #     ip_address = dns.resolver.resolve(search, 'A').rrset[0].to_text()
    # except dns.resolver.NoAnswer:
    #     ip_address = 'No answer'

    # ip6=socket.getaddrinfo(search, None, socket.AF_INET6)[0][4][0]
    # untag
    # search = request.POST.get('search')
    # search = 'www.nic.in'
    # search = "'" + search + "'"
    # ip_address = dns.resolver.Resolver()
    # answers = ip_address.resolve(search, 'A').rrset[0].to_text()
    # answers = dns.resolver.Resolver.resolve(search, 'A')
    # context = {"ip_address": answers}
    # print(answers)
    # se = search
    # ip = {"ip_address": answers}
    # hosti = {"hostname": se}
    # hosti = {"hostname": ast.literal_eval("{'search'}")}
    # context={"data": data}
    # return render(request, 'index.html', {"hostname": se}, {"ip_address": answers})
    # return render(request, 'index.html', context)
    # return render(request, 'index.html', ip)


# def home_view(request):
#     return render(request, 'home.html')
#
#
# def signup_view(request):
#     form = SignUpForm(request.POST)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#         else:
#             form = UserCreationForm()
#
#         return render(request, 'signup.html', {'form': form})

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegisterForm
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context
#
#
# def index(request):
#     return render(request, 'user/index.html', {'title':'index'})
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             ######################### mail system ####################################
#             htmly = get_template('IPApp/Email.html')
#             d = {'username': username}
#             subject, from_email, to = 'welcome', 'your_email@gmail.com', email
#             html_content = htmly.render(d)
#             msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
#             msg.attach_alternative(html_content, "text/html")
#             msg.send()
#             ##################################################################
#             messages.success(request, f'Your account has been created ! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'IPApp/register.html', {'form': form, 'title': 'reqister here'})
#
#
# ################ login forms###################################################
#
# def Login(request):
#     if request.method == 'POST':
#
#         # AuthenticationForm_can_also_be_used__
#
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             form = login(request, user)
#             messages.success(request, f' welcome {username} !!')
#             return redirect('index')
#         else:
#             messages.info(request, f'account done not exit plz sign in')
#     form = AuthenticationForm()
#     return render(request, 'IPApp/login.html', {'form': form, 'title': 'log in'})


from django.shortcuts import render
import dns
import dns.resolver


def index(request):
    if request.method == 'POST':

        search = request.POST.get('search')
        # search = 'www.google.com'
        # search = "'" + search + "'"
        ip_address = dns.resolver.Resolver()
        IPv4 = ip_address.resolve(search, 'A').rrset[0].to_text()
        IPv6 = ip_address.resolve(search, 'AAAA').rrset[0].to_text()
        # answers = dns.resolver.Resolver.resolve(search, 'A').rrset[0].to_text()
        # ip = {"ip_address": answers}
        # host = {"hostname": search}
        return render(request, 'index.html', {"ipv4": IPv4, "ipv6": IPv6, "hostname": search})
    else:
        return render(request, 'index.html')


# from django.shortcuts import render
# import socket
#
#
# def index(request):
#     # search = request.POST.get('search')
#     search = 'www.google.com'
#     # search = "'" + search + "'"
#     # ip_address = dns.resolver.Resolver()
#     # answers = ip_address.resolve(search, 'A').rrset[0].to_text()
#     answers = socket.getaddrinfo(search ,0,0,0,0)
#     # ip = {"ip_address": answers}
#     # host = {"hostname": search}
#     return render(request, 'index.html', {"ip_address": answers, "hostname": search})
