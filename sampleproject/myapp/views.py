from django.shortcuts import render, HttpResponse

def index(self, request):
    return HttpResponse("hello")
