from django.shortcuts import render, redirect
from system.models import Sidebar
from django.template import RequestContext
from collections import defaultdict
from django.contrib import auth
from django.contrib.auth.models import Permission


def index(request):
    return render(request, 'index.html', {'permissions': side_bar(request)})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'login_fail': 0})
    user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/')
    else:
        return render(request, 'login.html', {'login_fail': 1})


def logout(request):
    auth.logout(request)
    return redirect('/login/')


def lock(request):
    name = request.user.employee.full_name()
    username = request.user.get_username()
    auth.logout(request)
    return render(request, 'lockscreen.html', {'name': name, 'username': username})


def dashboard(request):
    return render(request, 'dashboard.html', {})


def side_bar(request):
    side_bars = []
    permissions = [(permission.split('.')[0], permission.split('_')[1])
                   for permission in request.user.get_all_permissions()]
    for sidebar in Sidebar.objects.all():
        for content in sidebar.content.all():
            if (content.app_label, content.model) in permissions:
                side_bars.append(sidebar)
    return permission_tree(side_bars)


def permission_tree(permissions):
    permission_dic = defaultdict(list)
    for permission in permissions:
        if not permission.parent and permission not in permission_dic.keys():
            permission_dic[permission]
        else:
            permission_dic[permission.parent].append(permission)
    # order matters
    permission_list = permission_dic.items()
    permission_list = [(x[0], sorted(x[1], key=lambda d: d.order)) for x in permission_list]
    return sorted(permission_list, key=lambda (k, v): (k.order, v))


def common_context(request):
    return {
        "path": request.path,
        "sidebars": side_bar(request)
    }


def test(request):
    return render(request, 'test.html', {})
