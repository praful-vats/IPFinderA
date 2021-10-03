from django.shortcuts import render, HttpResponse
import pandas as pd
from .models import FilesUpload


def home(request):
    if request.method == "POST":
        file = request.FILES["myFile"]
        csv = pd.read_csv(file)
        document = FilesUpload.objects.Create(file=file2)
        document.save()
        return HttpResponse("Saved")
    return render(request, "index.html")
