from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from system.models import Label
from system.forms import LabelForm


class LabelCreateView(CreateView):
    form_class = LabelForm
    template_name = 'system/label/modal.html'

    def get_context_data(self, **kwargs):
        context = super(LabelCreateView, self).get_context_data(**kwargs)
        context['url'] = '/system/label/ajax/add/'
        return context

    def form_valid(self, form):
        form.save()
        return render(self.request, 'system/label/body.html', {'labels': Label.objects.all(),
                                                               'success': True})


class LabelUpdateView(UpdateView):
    form_class = LabelForm
    template_name = 'system/label/modal.html'
    context_object_name = 'spec_label'

    def get_object(self, queryset=None):
        return Label.objects.get(id=self.kwargs['label'])

    def get_context_data(self, **kwargs):
        context = super(LabelUpdateView, self).get_context_data(**kwargs)
        context['url'] = '/system/label/ajax/mod/%d/' % self.object.id
        return context

    def form_valid(self, form):
        form.save()
        return render(self.request, 'system/label/body.html', {'labels': Label.objects.all(),
                                                               'success': True})


@permission_required('system.delete_label')
def label_delete(request):
    Label.objects.get(id=request.POST.get('label_id')).delete()
    labels = Label.objects.all()
    return render(request, 'system/label/body.html', {'labels': labels,
                                                      'success': True})