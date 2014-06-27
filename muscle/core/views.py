# coding: utf-8
from django.shortcuts import render

def home(request):
    """
    	Esse método tem por objetivo exibir o template da página inicial
    """

    return render(request, 'home/index.html')

def search(request):
    """
    	Esse método tem como objetivo a busca das informações na placa
    """

    return render(request, 'board/search.html')