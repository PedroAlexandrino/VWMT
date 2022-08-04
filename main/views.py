from django.shortcuts import render


def home(request):
    # print("Tas aqui")
    return render(request, "main/home.html")
