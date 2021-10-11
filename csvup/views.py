from django.shortcuts import render
import dns
import dns.resolver
import requests
from docutils.nodes import
import pandas as pd


# def csvu(request):
#     with open('ex.csv', 'r', newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for rows in reader:
#             row = str(rows)
#             row = row.strip('[]\'')
#             # ip_address = dns.resolver.Resolver()
#             # IPv4 = ip_address.resolve(row, 'A').rrset[0].to_text()
#             # IPv6 = ip_address.resolve(row, 'AAAA').rrset[0].to_text()
#             # url = "https://" + row
#             # page = requests.get(url)
#             # pagi = page.status_code
#             # hashi = hash(row)
#             try:
#                 reversed_dns = socket.gethostbyaddr(row)
#                 if str.__contains__(reversed_dns[0], 'googlebot.com') or str.__contains__(reversed_dns[0], 'google.com'):
#                     temp_ip = socket.gethostbyaddr(str(reversed_dns[2]).strip("'[]'"))
#                     if reversed_dns == temp_ip:
#                         googlebot.append(reversed_dns[0])
#                     else:
#                         nongooglebot.append(reversed_dns[0])
#                 else:
#                     nongooglebot.append(reversed_dns[0])
#             except:
#                 pass
#             csvfile.close()
#     return render(request, 'index.html', {"ipv4": IPv4, "ipv6": IPv6, "hostname": search, "hash": hashi, "down": pagi})
#     else:
#         return render(request, 'index.html')
#
#
#
# # Create your views here.
# ip_address = dns.resolver.Resolver()
# try:
#     IPv4 = ip_address.resolve(row, 'A').rrset[0].to_text()
#     if str.__contains__(reversed_dns[0], 'googlebot.com') or str.__contains__(reversed_dns[0], 'google.com'):
#         temp_ip = socket.gethostbyaddr(str(reversed_dns[2]).strip("'[]'"))
#         if reversed_dns == temp_ip:
#             googlebot.append(reversed_dns[0])
#         else:
#             nongooglebot.append(reversed_dns[0])
#     else:
#         nongooglebot.append(reversed_dns[0])
# except:
#     pass
# csvfile.close()
def csvu(request):
    data = csv


