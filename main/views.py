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

def Get_Ajax_Logs(request):
	if(os.path.exists("logs.txt")):
		with open('logs.txt','r') as f:
		    logs = f.read()

		logs = logs.replace("\n","<br />")
	else:
		logs = ""

	return render(request, 'main/ajax_index.html', {'logs': logs}) 	

class ChangeLanguageView(TemplateView):

    template_name = 'main/change_language.html'


def ActiveTicketsView(request):

	with open('pkl/ticketsReplied.pkl','rb') as f:
	    tickets_r = pickle.load(f)

	return render(request, 'main/active_tickets.html', {'tickets': tickets_r}) 


def FlowJourneysView(request):

	template_name = 'main/flow_journeys.html'
	with open('status.txt', 'r') as f:
		status = f.read()
	
	return render( request, template_name, {'status': status} )

def ClusterView(request):

	template_name = 'main/cluster.html'
	
	return render( request, template_name )

def Get_Journey_Image(request):
	
	template_name = 'main/ajax_journeys.html'
	with open('status.txt', 'r') as f:
		status = f.read()
	
	return render( request, template_name, {'status': status} )


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


def TemplatesView(request):

	templates = {
		'template1':"""
			Hello,

			Thanks for contacting us.
			Your ticket ID is: %s. 

			We'll answer your query as soon as posible.

			Have a great Day,
			This message was generated automatically by our A.I. agent

		 """,
		 'template2':"""
		 	Template 2 text
		 """,
		 'template3':"""
		 	Template 3 text
		 """


	}

	return render(request, 'main/templates.html',{'templates':templates}) 
