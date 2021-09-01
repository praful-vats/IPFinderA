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

from django.shortcuts import render
import dns
import dns.resolver


def index(request):
    search = request.POST.get('search')
    print(search)
    # ip_address = dns.resolver.Resolver.resolve(search, "A")
    # ip_address = dns.resolver.query(search, "A")
   #untag
    ip_address = dns.resolver.Resolver()
    answers = ip_address.resolve(search, 'A').rrset[0].to_text()
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
#untag
    context = {"ip_address": answers}
    # context={"data": data}
    return render(request, 'index.html', context)

