from apps.personal.models import Personal
from apps.personal.forms import PersonalForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# ------------------------------------------------------------------------------------>
# view Personal

class PersonalList(ListView):
    model = Personal
    template_name = 'personal/personal_list.html'
    context_object_name = 'personal_list'
    queryset = Personal.objects.all()


class PersonalNew(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'personal/personal_form.html'
    success_url = reverse_lazy('personal:personal_list')


class PersonalUpdate(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'personal/personal_form.html'
    success_url = reverse_lazy('personal:personal_list')


class PersonalDelete(DeleteView):
    model = Personal
    form_class = PersonalForm
    template_name = 'personal/personal_delete.html'
    success_url = reverse_lazy('personal:personal_list')



