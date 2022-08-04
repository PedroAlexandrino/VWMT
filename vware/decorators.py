from django.http import HttpResponse
from django.shortcuts import redirect

from django.urls import path
from .views import *


class MetaRoutes:
    routes = []


def route(endpoint: str, name: str):
    def decorator(func):
        path_obj = path(endpoint, func, name=name)
        MetaRoutes.routes.append(path_obj)
        return func

    return decorator


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.filter(name__in=allowed_roles).exists():
                group = request.user.groups.all()[0].name

            if group == "admin":
                return view_func(request, *args, **kwargs)
            if group == None:
                return redirect("vware:armazem")

        return wrapper_func

    return decorator
