# from django.shortcuts import render
# import ipapi
#
#
# def Index(request):
#     search = request.POST.get('search')
#
#     data = ipapi.location(ip=search, output='json')
#
#     context = {"data": data}
#
#     return render(request, 'index.html', context)
from django.shortcuts import render
import dns.resolver


def Index(request):
    search = request.POST.get('search')
    print('search='+search)
    ip_address = dns.resolver.resolve(search, "A")
    context = {"ip_address": ip_address}
    return render(request, 'index.html', context)
