from django.shortcuts import render, redirect
from oa_model.models import OaUser
from django.template import RequestContext
from django.http import HttpResponse
from hashlib import md5


def index(request):
    return render(request, 'index.html', {},
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
    return HttpResponse("1111111aaaaa1")


def check_password(encrypted, password):
    return encrypted == md5(password).hexdigest()


def login_status(request):
    try:
        return request.session['user_id']
    except Exception, e:
        print e
        return None


def common_context(request):
    user_id = request.session.get('user_id')
    real_name = request.session.get('real_name')
    username = request.session.get('username')
    return {
        "user_id": user_id,
        "real_name": real_name,
        "username": username
    }