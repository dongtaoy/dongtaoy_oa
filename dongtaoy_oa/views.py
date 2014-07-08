from django.shortcuts import render, redirect
from oa_model.models import OaUser, OaGroupPermission, OaUserGroup
from django.template import RequestContext
from django.http import HttpResponse
from collections import defaultdict
from hashlib import md5


def index(request):
    return render(request, 'index.html', {'permissions': side_bar(request)},
                  context_instance=RequestContext(request, processors=[common_context]))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'login_fail': 0})
    try:
        user = OaUser.objects.get(username=request.POST.get('username'))
        if check_password(user.password, request.POST.get('password')):
            request.session['user_id'] = user.id
            request.session['real_name'] = user.realname
            request.session['username'] = user.username
            return redirect('/')
        else:
            return render(request, 'login.html', {'login_fail': 1})
    except Exception, ex:
        print ex
        return render(request, 'login.html', {'login_fail': 1})


def logout(request):
    del request.session['user_id']
    del request.session['real_name']
    del request.session['username']
    return redirect('/login/')


def lock(request):
    del request.session['user_id']
    return render(request, 'lockscreen.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))


def dashboard(request):
    return render(request, 'dashboard.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))


def check_password(encrypted, password):
    return encrypted == md5(password).hexdigest()


def login_status(request):
    try:
        return request.session['user_id']
    except Exception, e:
        print e
        return None


def side_bar(request):
    return get_all_permissions(request)


def get_all_permissions(request):
    groups = [x.group for x in OaUserGroup.objects.filter(user=OaUser.objects.get(id=request.session.get('user_id')))]
    permissions = list(set([x.permission for x in OaGroupPermission.objects.filter(group__in=groups)]))
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
    #return sorted(permission_dic.iteritems(), key=lambda (k, v): (k.order, v))


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


