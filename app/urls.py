from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, ChangeLanguageView, ActiveTicketsView, FlowJourneysView, MailDataView, TemplatesView, Get_Journey_Image

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView, name='index'),

    path('tickets/', ActiveTicketsView , name="active_tickets"),
    path('journey/', FlowJourneysView, name="flow_journeys"),
    path('mail-data/', MailDataView, name="mail_data"),
    path('templates/', TemplatesView, name="templates"),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),
    path('ajax_journey/', Get_Journey_Image, name='ajax_journey_image'),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
