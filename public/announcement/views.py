# encoding=utf-8
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect
from django.db import transaction
from django.utils import timezone
from public.forms import MessageForm
from public.models import MessageTo


# def announcement_publish_index(request):
#     groups = Department.objects.all()
#     return render(request, 'public/announcement/publish.html', {'groups': groups},
#                   context_instance=RequestContext(request, processors=[common_context]))


# def announcement_save(request):
#     print request.FILES
#     return HttpResponse(1)

class AnnouncementCreateView(SuccessMessageMixin, CreateView):
    template_name = 'public/announcement/publish.html'
    form_class = MessageForm
    success_url = '/public/announcement/publish/'
    success_message = '%(subject)s发布成功'.decode('utf-8')

    def get_context_data(self, **kwargs):
        context = super(AnnouncementCreateView, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
        with transaction.atomic():
            super(AnnouncementCreateView, self).form_valid(form)
            self.object.fromUser = self.request.user
            self.object.time = timezone.now()
            self.object.save()
            groups = self.request.POST.getlist('groups')
            # ALL USERS
            if '0' in groups:
                for user in User.objects.filter(is_active=1):
                    MessageTo.objects.create(message=self.object, user=user)
            else:
                for user in User.objects.filter(groups__id__in=groups):
                    MessageTo.objects.create(message=self.object, user=user)
        return redirect(self.success_url)

