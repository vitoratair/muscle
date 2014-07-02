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

def statistics(request):

    heart = Structure.objects.filter(Q(dataType=1))[:20]

    aux = ''
    for i in heart:
        aux = str(aux) + "," + str(i.dataPayload)
    aux = str(aux) + ']'
    aux = "[" + str(aux[1:])
    heart = aux

    aux = ''
    for i in range(0,19):
        aux = str(aux) + " , " + str(i)

    aux = str(aux) + ']'
    aux = "[" + str(aux[2:])
    labelHeart = aux

    axisX = Structure.objects.filter(Q(dataType=10))[:20]
    axisY = Structure.objects.filter(Q(dataType=11))[:20]
    axisZ = Structure.objects.filter(Q(dataType=11))[:20]

    aux = ''
    for i in range(0,20):
        aux = str(aux) + ",[" + str(axisX[i].dataPayload) + ',' + str(axisY[i].dataPayload) + ',' + str(axisZ[i].dataPayload) + "]"

    aux = str(aux)
    aux = str(aux[1:])
    axis = aux

    return render(request, 'board/statistics.html', {'heart': heart, 'labelHeart': labelHeart, 'axis': axis})





