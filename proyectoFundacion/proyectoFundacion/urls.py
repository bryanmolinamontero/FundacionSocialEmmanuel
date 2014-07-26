from django.conf.urls import patterns, include, url

from fundacion.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from proyectoFundacion import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyectoFundacion.views.home', name='home'),
    # url(r'^proyectoFundacion/', include('proyectoFundacion.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:





    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^base/$', base),
    url(r'^nosotros/$', nosotros),
    url(r'^proyectos/ceti/$', ceti),
    url(r'^proyectos/etimendi/$', etimendi),
    url(r'^proyectos/duenademi/$', duenademi),
    url(r'^proyectos/jetsemani/$', jetsemani),
    url(r'^programas/$', programas),
    url(r'^contacto/$', contacto),
    url(r'^enviarCorreo/$', enviarCorreo),
    url(r'^voluntario/$', voluntario),
    url(r'^multimedia/$', multimedia),

    url(r'^reciclaFuturo/$', reciclaFuturo),
    url(r'^miAbueloAdoptivo/$', miAbueloAdoptivo),
    url(r'^hermanoMayor/$', hermanoMayor),
    url(r'^correoPrograma/$', correoPrograma),
    url(r'^nuevoVoluntario/$', nuevoVoluntario),
    #ddd
    url(r'^ver_noticia/^', verNoticia),
    url(r'^ver_noticia/(?P<id_noticia>.*)/$',ver_noticia,name="ver_noticia"),
   # url(r'^tinymce/', include('tinymce.urls')),

    url(r'^archivos/$', archivos),

    url(r'^ingresarPersona/$', ingresarPersona),
)


handler404 = 'fundacion.views.handler404'