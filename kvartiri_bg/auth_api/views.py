from django.shortcuts import render
from .forms import UserModelSerializer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
# Create your views here.

class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        serializer = UserModelSerializer()
        return Response({'serializer': serializer})
    

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        serializer = UserModelSerializer()
        return Response({'serializer': serializer})