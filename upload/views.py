from django.shortcuts import render, HttpResponse
import pandas as pd
# from .models import FilesUpload


def upload_file_view(request):
    if request.method == "POST":
        file = request.FILES["myFile"]
        csv = pd.read_csv(file)
        print(csv.head())

        return HttpResponse("Saved")
    return render(request, "index.html")



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
