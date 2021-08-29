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

from django.shortcuts import render
import dns.resolver


def index(request):
    search = request.POST.get('search')
    my_resolver = dns.resolver.Resolver()
    ip_address = my_resolver.resolve(search, "A")[0]
    # ip_address = dns.resolver.Resolver.resolve(search, 'A')
    # for i in ip_address:
    ip = ip_address.to_text()
    context = {"ip_address": ip}
    return render(request, 'index.html', context)
