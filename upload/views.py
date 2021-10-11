from django.shortcuts import render, redirect
import pandas as pd
# from .models import FilesUpload
from dns import ipv4
from dns import ipv6
from IPApp import


def filo(request):
    if request.method == "POST":
        file = request.FILES["myFile"]
        csv = pd.read_csv(file)
        df1 = csv["hostnames"]
        df1.index = pd.DataFrame({"IPv4": {{ipv4}}
                                  {"IPv6": {{ ipv6 }}}
                                      {"hash": {{ hashi }}}


                                  })
        return redirect('/upload/uplo/')
        # return HttpResponse("Saved")
    else:
        return render(request, 'uplo.html')



# import socket
# import os
# import csv
# name = {}
# CI = {}
# with open('file1.csv', 'r', newline='') as csvinput:
#     reader = csv.DictReader(csvinput)
#
#     # status = [row['FQDN'] for row in rows]
#
# with open('file2.csv', 'w', newline='') as csvoutput:
#     fieldnames = ['CI_Name', 'FQDN']
#     output = csv.DictWriter(csvoutput, fieldnames=fieldnames)
#     output.writeheader()
#
# for rows in reader:
#     CI = rows['CI_Name']
#     name = socket.getfqdn(CI)
#     with open('file2.csv', 'a', newline='') as csvoutput:
#        output = csv.writer(csvoutput)
#        output.writerows([[CI] + [name]])
