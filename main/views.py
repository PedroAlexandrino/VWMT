from django.shortcuts import render
from django.http import JsonResponse
from shippers.models import *
from datetime import datetime

def home(request):
    # print("Tas aqui")
    """  updates = UpdatesProj.objects """
    return render(
                request,
                "main/home.html",
                {#"updates" : updates,
                }
                
            )

def addUpdate(request):
    UpdatesProj(update=request.POST["update"],date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return JsonResponse({"message": "OK"})

def updatesJson(*request):
    updates = UpdatesProj.objects.all()
    dados_list = [item.to_dict() for item in updates]
    print("POST---)",len(dados_list),dados_list, "\n")
    return JsonResponse({"message": "OK","updates" : dados_list})