from django.shortcuts import render, redirect
from system.models import Sidebar
from django.template import RequestContext
from collections import defaultdict
from django.contrib import auth
from django.contrib.auth.models import Permission


def index(request):
    return render(request, 'index.html', {'permissions': side_bar(request)},
                  context_instance=RequestContext(request, processors=[common_context]))


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
    return render(request, 'lockscreen.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))


def dashboard(request):
    return render(request, 'dashboard.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))


def side_bar(request):
    return permission_tree(Sidebar.objects.all())


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
    user_id = request.session.get('user_id')
    real_name = request.session.get('real_name')
    username = request.session.get('username')
    return {
        "user_id": user_id,
        "real_name": real_name,
        "username": username,
        "path": request.path,
        "sidebars": side_bar(request)
    }


def test(request):
    return render(request, 'test.html', {})
