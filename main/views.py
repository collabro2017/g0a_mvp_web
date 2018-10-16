from django.views.generic import TemplateView
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render


import pickle
import os

# class IndexPageView(TemplateView):
#     template_name = 'main/index.html'

def IndexPageView(request):

	if(os.path.exists("logs.txt")):
		with open('logs.txt','r') as f:
		    logs = f.read()

		logs = logs.replace("\n","<br />")
	else:
		logs = ""

	return render(request, 'main/index.html', {'logs': logs}) 

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
		try:
			mailData = pickle.load(f)
		except Exception as e:
			print(e)
			mailData = {}


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
