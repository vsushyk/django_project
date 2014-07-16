# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from contacts.models import Contact
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import DeleteView

class ListContactView(ListView):

	model = Contact
	template_name = 'contact_list.html'


class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwards):
	
	context = super(CreateContactView, self).get_context_data(**kwards)
	context['action'] = reverse('contacts-new')

	return context

class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit', kwargs={'pk': self.get_object().id})

        return context

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')
