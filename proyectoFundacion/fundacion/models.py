from django.db import models

from django.contrib import admin
#from tinymce import models as tinymce_models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, blank=True)
    edad = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'persona'

    def __unicode__(self):
        return '%d, %s, %d' % (self.id, self.nombre, self.edad)

class Inicio(models.Model):

    titulo = models.CharField(max_length=200 , null= False)
    subtitulo = models.CharField(max_length=100 , null= False)
    descripcion = models.TextField(null=False)
    imagenInicio = models.ImageField(upload_to='subida' , null=True)

    class Meta:
        verbose_name_plural = "Inicio"

class InicioAdmin(admin.ModelAdmin):
    list_display =( 'titulo' , 'subtitulo', 'descripcion')


    def __unicode__(self):
        return '%s, %s, %s' % (self.titulo, self.subtitulo, self.descripcion)

admin.site.register(Inicio, InicioAdmin)

class Nosotros(models.Model):

    mision = models.TextField(null=False)
    imagenMision = models.ImageField(upload_to='subida' , null=True)
    vision = models.TextField(null=False)
    imagenVision = models.ImageField(upload_to='subida' , null=True)
    objetivo = models.TextField(null=False)
    imagenObjetivo = models.ImageField(upload_to='subida' , null=True)

    class Meta:
        verbose_name_plural = "Nosotros"

class NosotrosAdmin(admin.ModelAdmin):
    list_display =( 'mision' , 'vision', 'objetivo')
    #list_filter = ('titulo',)
    #search_fields = ('titulo',)


    def __unicode__(self):
        return '%s, %s, %s' % (self.mision, self.vision, self.objetivo)


admin.site.register(Nosotros, NosotrosAdmin)


class Programas(models.Model):
    titulo = models.CharField(max_length=100 , null=False)
    descripcion = models.TextField(null=False)
    boton = models.CharField(max_length=50, null=False)
    imagen = models.ImageField(upload_to='subida', null=False)

    class Meta:
        verbose_name_plural = "Programas"

    def __unicode__(self):
        return '%s, %s' % (self.titulo, self.descripcion)

class ProgramasAdmin(admin.ModelAdmin):
    list_display =( 'titulo' , 'descripcion', 'boton')
    #list_filter = ('titulo',)
    search_fields = ('titulo',)

admin.site.register(Programas, ProgramasAdmin)


class Contacto(models.Model):
    oficina = models.CharField(max_length=100,null=False)
    cp = models.CharField(max_length=50,null=False)
    mail = models.EmailField(max_length=50)
    tel = models.CharField(max_length=50,null=False)
    fax = models.CharField(max_length=50,null=False)
    cel = models.CharField(max_length=50,null=False)

    class Meta:
        verbose_name_plural = "Contacto"

    def __unicode__(self):
        return '%s , %s , %s , %s , %s , %s ' % (self.oficina , self.cp , self.mail , self.tel , self.fax , self.cel)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('oficina', 'cp', 'mail', 'tel', 'fax', 'cel')

admin.site.register(Contacto,ContactoAdmin)


class Noticias(models.Model):
    titulo=models.CharField(max_length=200,help_text='Ingrese el titulo de la noticia...')
    fecha=models.DateField(auto_now=True)
    imagen=models.ImageField(upload_to='noticias',help_text='Seleccione la imagen para la noticia...', null=True,blank=True)
    imagen1=models.ImageField(upload_to='noticias',help_text='Opcional...Seleccione una imagen.', null=True,blank=True)
    imagen2=models.ImageField(upload_to='noticias',help_text='Opcional...Seleccione una imagen.', null=True,blank=True)
    contenido=models.TextField(help_text='Escribir el contenido de la nueva noticia...')
    #contenido = tinymce_models.HTMLField()

    class Meta:
        verbose_name_plural = "Noticia"

    def __unicode__(self):
        return "%s , %s , %s, %s, %s, %s"%(self.id,self.titulo, self.imagen,self.imagen1,self.imagen2,self.contenido)


class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'contenido')
    search_fields = ('fecha',)
admin.site.register(Noticias, NoticiasAdmin)


class videos(models.Model):
    titulo = models.CharField(max_length=200,help_text='Ingrese titulo del video')
    link = models.TextField(help_text='Pegar el codigo generado desde la opcion Insertar del video de youtube')

    class Meta:
        verbose_name_plural = "Videos"


    def __unicode__(self):
        return "%s, %s" % (self.titulo , self.link)

class videosAdmin(admin.ModelAdmin):
    list_display = ("titulo" , "link")

admin.site.register(videos,videosAdmin)



#SUBIDA DE ARCHIVOS2
class archivos2(models.Model):
    titulo=models.CharField(max_length=200,help_text='Ingrese el titulo del archivo...')
    fecha=models.DateField(auto_now=True)
    archivo=models.FileField(upload_to='archivos',help_text='Seleccione un archivo a subir...', null=True,blank=True)
    contenido=models.TextField(help_text='Escribir descripcion del archivo...')
    #contenido = tinymce_models.HTMLField()

    class Meta:
        verbose_name_plural = "Archivos"

    def __unicode__(self):
        return "%s , %s , %s, %s, %s"%(self.id,self.titulo, self.fecha , self.archivo,self.contenido)


class archivos2Admin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'contenido')
    search_fields = ('fecha',)
admin.site.register(archivos2, archivos2Admin)
