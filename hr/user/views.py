from oa_model.models import OaUser, OaGroup
from django.shortcuts import render
from django.http import HttpResponse


# user index
def user_index(request):
    users = OaUser.objects.all()
    groups = OaGroup.objects.all()
    return render(request, 'hr/user/index.html', {'users': users,
                                                  'groups': groups})


# user detail
def user_detail(request):
    spec_user = OaUser.objects.get(id=request.GET.get('user_id'))
    users = OaUser.objects.all()
    groups = OaGroup.objects.all()
    return render(request, 'hr/user/modal.html', {'spec_user': spec_user,
                                                  'users': users,
                                                  'groups': groups})