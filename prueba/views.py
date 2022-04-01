import os
import psutil
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from prueba.serializers import PruebaSerializer, ActualizarSerializer,LoggerSerializer,LoggerSerializerComplete
from prueba.models import Prueba, Logger
from rest_framework.response import Response
from django.views.generic import ListView, TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from django.urls import reverse_lazy, reverse
from django.db.models import Max
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from braces.views import LoginRequiredMixin, CsrfExemptMixin

class ListPruebaAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer


class EstadoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    serializer_class = ActualizarSerializer
    
    def get_queryset(self):
        luz = self.kwargs['pk']
        queryset = Prueba.objects.filter(Luz__icontains=luz)
        return queryset

class CreatePruebaAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

class UpdatePruebaAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
   
    queryset = Prueba.objects.all()
    serializer_class = ActualizarSerializer


class DeletePruebaAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

#formulario para crear nuevas luces.

class FormularioListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'editar.html'
    
    def get(self, request,pk):
        luz = get_object_or_404(Prueba, pk=pk)
        serializer = PruebaSerializer(luz)
        return Response({'serializer': serializer, 'luz': luz})
    
    def post(self, request, pk):
        luz = get_object_or_404(Prueba, pk=pk)
        serializer = PruebaSerializer(luz, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'luz': luz})
        serializer.save()
        print(reverse_lazy('luces_app:Luces'))
        return redirect(reverse_lazy('luces_app:Luces'))

#Puedo modificar, pero no agregar uno nuevo por lo que me es imprescindible
#crear un formulario que tome el valor mas alto, sume 1 y cree una nueva entrada

class FormularioListView2(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cargarnuevo.html'
    
    def get(self, request):
        #busco el sk mas alto
        max = Prueba.objects.aggregate(Max('Luz'))['Luz__max']
        #puleo el objeto con el sk mas alto
        luz = get_object_or_404(Prueba, pk=max)
        #lo serializo.
        serializer = PruebaSerializer(luz)
        #Le agrego una unidad mas
        luz.Luz = max + 1
        #muestro el formulario
        return Response({'serializer': serializer,'luz': luz})

    def post(self, request):
        #devuelta 
        max = Prueba.objects.aggregate(Max('Luz'))['Luz__max']
        luz = get_object_or_404(Prueba, pk=max)
        serializer = PruebaSerializer(luz,data=request.data)
        print(serializer)
        luz.Luz = max + 1
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'luz': luz})
        serializer.save()
        return redirect(reverse_lazy('luces_app:Luces'))

#vieja pagina de encendido y apagado
class LucesListView2(ListView):
    model = Prueba
    template_name = "luces2.html"
    context_object_name = 'luz'

#vista que renderiza la pagina con js.
class LucesListView3(ListView):
    model = Prueba
    template_name = "luces3.html"
    context_object_name = 'luz'
    
#esta es a la que llama cuando ya esta renderizada la anterior y la usa js para ver el cada luz. 
class ListPruebaAPIView2(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    serializer_class = PruebaSerializer
    def get_queryset(self):
        encendido = self.request.query_params.get('encendido',None)
        id =  self.request.query_params.get('id',None)
        
        if(encendido == ""):
            print(encendido)
            return Prueba.objects.all()
        elif(id):
            if (id == '0'):  
                return Prueba.objects.all()
            else:
                return Prueba.objects.filter(Luz = id)          
        else:
            print("entro al else")
            return Prueba.objects.filter(encendido = encendido)
        


class PanelView(TemplateView):
    template_name = "panel.html"
    
    #para pasar un contexto o sea datos a la pagina debemos agregar esto. 
    def datos():
        cpu = {}
        load1, load5, load15 = psutil.getloadavg()
        cpu['load15'] = (load15/os.cpu_count()) * 100
        load15, load30, load60 = psutil.getloadavg()
        cpu['load60'] = (load15/os.cpu_count()) * 100
        cpu['freq'] = psutil.cpu_freq()[0]
        cpu['ram'] =  psutil.virtual_memory()[2]


        return cpu
        

    
    def get_context_data(self, *args, **kwargs):
        context = super(PanelView, self).get_context_data(*args, **kwargs)
        context['name'] = 'Gryffindor'
        context['cpu']  = PanelView.datos
        return context


#################################################################
#Esta vista me permitira guardar la info de loggien de cada luz.
####################################################################


class CreateLoggerAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Logger.objects.all()
    serializer_class = LoggerSerializer

class ListLoggerAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Logger.objects.all().order_by('-id')
    serializer_class = LoggerSerializerComplete
