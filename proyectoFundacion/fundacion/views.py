# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render

from django.core.mail import EmailMessage
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext

from models import *

emisor = "fundacionsocialemmanuel@gmail.com"
destinatario = "bryanux@hotmail.com"


def index(request):

    datos = Inicio.objects.all()
    extraerNoticia=Noticias.objects.all().order_by("-id")
    paginator = Paginator(extraerNoticia, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {"contacts": contacts , "inicio":datos})

def verNoticia(request):
    return HttpResponseRedirect('/index/')


def ver_noticia(request, id_noticia):

    try:
        noticia = Noticias.objects.get(id=id_noticia)
        if request.method == 'GET':
            valores = Noticias.objects.all()
            #form_noticia = noticia(initial={'titulo':noticia.titulo,'fecha':noticia.fecha,'imagen':noticia.imagen,'contenido':noticia.contenido})
            #args = {'form':form_noticia,'noticia':Noticias}
            return render_to_response('ver_noticia.html', RequestContext(request, locals()))
    except Exception:
        return HttpResponseRedirect('/index/')



def base(request):
    return render_to_response('base.html')



def nosotros(request):

    datos = Nosotros.objects.all()
    return render_to_response('nosotros.html' , {"nosotros":datos})

def ceti(request):
    return render_to_response('ceti.html')

def etimendi(request):
    return  render_to_response('etimendi.html')

def duenademi(request):
    return render_to_response('duenademi.html')

def jetsemani(request):
    return render_to_response('jetsemani.html')

def programas(request):
    datos = Programas.objects.all()
    return render_to_response('programas.html' , {"programas":datos})


def contacto(request):
    datos = Contacto.objects.all()
    return render_to_response('contacto.html', {"contacto":datos})

def voluntario(request):
    return render_to_response('voluntario.html')





def enviarCorreo(request):


    if request.method=='POST':

        nombre =  request.POST['txtNombre']
        correo =  request.POST['txtCorreo']
        telefono =  request.POST['txtTelefono']
        mensaje =  request.POST['txtContenidoMensaje']

        subject = 'CONTACTO'
        text_content = 'Mensaje...nLinea 2nLinea3'

        html_content = '<b>' \
                       'Correo FSE </br></br>' \
                       'Nombres: %s </br></br>' \
                       'Correo: %s </br></br>' \
                       'Telefono: %s </br></br>' \
                       'Mensaje: %s </br></br>' \
                       '</b>' % (nombre , correo, telefono, mensaje)
        from_email = '"Correo FSE" <%s>' % emisor
        to = destinatario
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponseRedirect('/contacto/')
    else:
        return HttpResponseRedirect('/contacto/')


def nuevoVoluntario(request):


    if request.method=='POST':

        nombre =  request.POST['txtNombre']
        apePaterno =  request.POST['txtApellidoPaterno']
        apeMaterno =  request.POST['txtApellidoMaterno']
        correo =  request.POST['txtCorreo']
        telefono =  request.POST['txtTelefono']
        mensaje =  request.POST['txtContenidoMensaje']

        subject = 'NUEVO VOLUNTARIO'
        text_content = 'Mensaje...nLinea 2nLinea3'

        html_content = '<b>' \
                       'Correo FSE </br></br>' \
                       'Nombres: %s </br></br>' \
                       'Apellido Paterno: %s </br></br>' \
                       'Apellido Materno: %s </br></br>' \
                       'Correo: %s </br></br>' \
                       'Telefono: %s </br></br>' \
                       'Mensaje: %s </br></br>' \
                       '</b>' % (nombre ,apePaterno ,apeMaterno , correo, telefono, mensaje)
        from_email = '"Correo FSE" <%s>' % emisor
        to = destinatario
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponseRedirect('/contacto/')
    else:
        return HttpResponseRedirect('/contacto/')




def reciclaFuturo(request):

    if request.method=='POST':

        nombre = request.POST['txtNombre']
        telefono = request.POST['txtTelefono']

        subject = 'Recicla Futuro'
        text_content = 'Mensaje...nLinea 2nLinea3'

        html_content = '<b>' \
                       'NUEVO COLABORADOR </br></br>' \
                       'Programa: Recicla Futuro </br></br>' \
                       'Nombres: %s </br></br>' \
                       'Telefono: %s </br></br>' \
                       '</b>' % (nombre , telefono)
        from_email = '"PROGRAMA" <%s>' % emisor
        to = destinatario
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponseRedirect('/programas/')

    else:
        return HttpResponseRedirect('/programas/')


def miAbueloAdoptivo(request):

    if request.method=='POST':
        nombre = request.POST['txtNombre']
        telefono = request.POST['txtTelefono']

        subject = 'Mi abuelo Adoptivo'
        text_content = 'Mensaje...nLinea 2nLinea3'

        html_content = '<b>' \
                       'NUEVO COLABORADOR </br></br>' \
                       'Programa: Mi Abuelo Adoptivo </br></br>' \
                       'Nombres: %s </br></br>' \
                       'Telefono: %s </br></br>' \
                       '</b>' % (nombre , telefono)
        from_email = '"PROGRAMA" <%s>' % emisor
        to = destinatario
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponseRedirect('/programas/')
        #return render(request, 'programas.html')
    else:
        return HttpResponseRedirect('/programas/')



def hermanoMayor(request):

    if request.method=='POST':
        nombre = request.POST['txtNombre']
        telefono = request.POST['txtTelefono']

        subject = 'Hermano Mayor'
        text_content = 'Mensaje...nLinea 2nLinea3'

        html_content = '<b>' \
                       'NUEVO COLABORADOR </br></br>' \
                       'Programa: Hermano Mayor </br></br>' \
                       'Nombres: %s </br></br>' \
                       'Telefono: %s </br></br>' \
                       '</b>' % (nombre , telefono)
        from_email = '"PROGRAMA" <%s>' % emisor
        to = destinatario
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponseRedirect('/programas/')
    else:
        return HttpResponseRedirect('/programas/')



def correoPrograma(request):

    if request.method=='POST':
        nombre = request.POST['txtNombre']
        telefono = request.POST['txtTelefono']

        subject = request.POST['txtAsunto']
        text_content = 'Mensaje...nLinea 2nLinea3'

        html_content = '<b>' \
                       'NUEVO COLABORADOR </br></br>' \
                       'Programa: '+ subject +' </br></br>' \
                       'Nombres: %s </br></br>' \
                       'Telefono: %s </br></br>' \
                       '</b>' % (nombre , telefono)
        from_email = '"PROGRAMA" <%s>' % emisor
        to = destinatario
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponseRedirect('/programas/')
    else:
        return HttpResponseRedirect('/programas/')


def ingresarPersona(request):

     if request.method=='POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        guardarProvincia = Persona(nombre=nombre , edad=edad)
        guardarProvincia.save()
        datos = Persona.objects.all()
        return render_to_response('resultado.html',{"respuesta":datos , "mensaje":"<div class=\"alert alert-success\"> REGISTRO GUARDADO CORRECTAMENTE </div>"})
        #return render_to_response('ingresarProvincia.html',  {"mensaje":"<div class=\"alert alert-success\"> REGISTRO GUARDADO CORRECTAMENTE </div>"})


     else:

        return render(request, 'index.html')



def multimedia(request):
    datos = videos.objects.all()
    return render_to_response('multimedia.html' , {"datos":datos})


from django.shortcuts import render

def handler404(request):
    return render(request,'404.html')


def archivos(request):

    #datos = Inicio.objects.all()
    extraerArchivos=archivos2.objects.all().order_by("-id")

    paginator = Paginator(extraerArchivos, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('archivos.html', {"contacts": contacts})