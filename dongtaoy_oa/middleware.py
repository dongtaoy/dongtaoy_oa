from django.shortcuts import redirect

class AuthenticationMiddleware(object):
    def process_request(self, request):
        if request.path != '/login/':
            if request.user.is_authenticated() and request.user.is_active:
                pass
            else:
                return redirect('/login/')