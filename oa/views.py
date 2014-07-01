from django.shortcuts import render, redirect
from oa_model.models import OaUser
from hashlib import md5

def index(request):
    if login_status(request):
        print 'logged'
        return redirect('/#dashboard/')
    else:
        print 'failed'
        return redirect('/login/')


def dashboard(request):
    return render(request, 'dashboard.html', {})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'login_fail': 0})
    user = OaUser.objects.get(username=request.POST.get('username'))
    print md5(request.POST.get('password')).hexdigest()
    if check_password(user.password, request.POST.get('password')):
        print 'right'
        request.session['user_id'] = user.id
        return index(request)
    else:
        print 'wrong'
        return render(request, 'login.html', {'login_fail': 1})


def logout(request):
    return


def check_password(encrypted, password):
    return encrypted == md5(password).hexdigest()


def login_status(request):
    try:
        return request.session['user_id']
    except Exception, e:
        print e
        return None