from django.shortcuts import render


def index(request):
    if login_status(request):
        return render(request, 'index.html', {})
    else:
        return render(request, 'login.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})


def login(request):
    return


def logout(request):
    return


def check_password(request):
    return


def login_status(request):
    try:
        return request.SESSION['user_id']
    except Exception:
        print Exception
        return None