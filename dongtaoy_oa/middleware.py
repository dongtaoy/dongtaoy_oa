from django.shortcuts import redirect


class AuthenticationMiddleware(object):
    def process_request(self, request):   
        #print request.path    
        if request.path != '/login/':    
            if request.session.get('user_id') != None:
                pass
            else:
                return redirect('/login/')