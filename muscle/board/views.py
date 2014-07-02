# coding: utf-8
from django.shortcuts import render
from muscle.board.library.readData import ReadData
from models import Structure
from django.db.models import Q

def home(request):

    return render(request, 'board/search.html')

def search(request):
    """
        Esse método tem como objetivo a busca das informações na placa
    """

    listInformation = []
    board = ReadData()
    data = board.getStart()

    for elements in data:

        if len(elements) != 0:
            listInformation.append(board.execParser(elements))

    board.saveData(listInformation)

    data = Structure.objects.filter(Q(dataType=1)| Q(dataType=10) | Q(dataType=11) | Q(dataType=12))

    return render(request, 'board/search.html', {'data': data})







