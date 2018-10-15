from django.views.generic import TemplateView
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render


import pickle

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

def ActiveTicketsView(request):

	with open('pkl/ticketsReplied.pkl','rb') as f:
	    tickets_r = pickle.load(f)


	return render(request, 'main/active_tickets.html', {'tickets': tickets_r}) 

class FlowJourneysView(TemplateView):
	template_name = 'main/flow_journeys.html'

def MailDataView(request):

	with open('pkl/emailsDict.pkl','rb') as f:
	    mailData = pickle.load(f)

	ticketsIDs = {}
	counter = 0

	for key, value in mailData.items():
		try:
			ticketsIDs[key] = value['id']
		except Exception:
			ticketsIDs[key] = "No need for id"

	return render(request, 'main/mail_data.html', {'dictionary': mailData, 'ticketsIDs': ticketsIDs}) 


class SettingsView(TemplateView):
	template_name = 'main/settings.html'
