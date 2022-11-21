from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ajay(request):
    return HttpResponse('<h1>ajay is most innocent guy</h1><style>h1{color:red;font-size:50pxpadding:80px;border:20px solid black;border-radius:20px;border-size:50px; </style>')
 