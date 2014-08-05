from django.shortcuts import render, redirect
from hr.models import Employee
from system.models import Permission
from django.template import RequestContext
from collections import defaultdict
from hashlib import md5


def index(request):
    return render(request, 'index.html', {'permissions': side_bar(request)},
                  context_instance=RequestContext(request, processors=[common_context]))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'login_fail': 0})
    try:
        user = Employee.objects.get(username=request.POST.get('username'))
        if check_password(user.password, request.POST.get('password'), user.salt):
            request.session['user_id'] = user.id
            request.session['real_name'] = user.realname
            request.session['username'] = user.username
            return redirect('/')
        else:
            return render(request, 'login.html', {'login_fail': 1})
    except Exception, ex:
        return render(request, 'login.html', {'login_fail': 1})


def logout(request):
    del request.session['user_id']
    del request.session['real_name']
    del request.session['username']
    return redirect('/login/')


def lock(request):
    return render(request, 'lockscreen.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))


def dashboard(request):
    return render(request, 'dashboard.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))


def check_password(encrypted, password, salt):
    return encrypted == md5(password+salt).hexdigest()


def login_status(request):
    try:
        return request.session['user_id']
    except Exception, e:
        return None


def side_bar(request):
    return get_all_permissions(request)


def get_all_permissions(request):
    groups = Employee.objects.get(id=request.session.get('user_id')).groups.all()
    permissions = Permission.objects.filter(group__in=groups)
    return permission_tree(permissions)


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
