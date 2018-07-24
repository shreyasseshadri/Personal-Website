# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def pdf_view(request):
    return redirect('/media/Resume.pdf')

    # with open('/media/Resume.pdf', 'r') as pdf:
    #     response = HttpResponse(pdf.read(), content_type='application/pdf')
    #     response['Content-Disposition'] = 'inline;filename=some_file.pdf'
    #     return response
    # pdf.closed

# from django.http import FileResponse, Http404
#
# def pdf_view(request):
#     try:
#         return FileResponse(open('Resume.pdf', 'rb'), content_type='application/pdf')
#     except:
#         # print("hello")
#         raise Http404()

def index(request):
    return render(request,'about/index.html',{})
# /home/shreyas/personal_website/about/templates/about/Resume.pdf
# /home/shreyas/personal_website/about/views.py
