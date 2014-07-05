# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from muscle.board.library.readData import ReadData
from models import Structure, Type
from django.db.models import Q

def home(request):

    return render(request, 'board/search.html')

def search(request):
    """
        Esse método tem como objetivo a busca das informações na placa
    """

    listInformation = []
    board = ReadData()
    # data = board.searchData()
    data = board.getStart()

    # for elements in data:

    #     if len(elements) != 0:
    #         listInformation.append(board.execParser(elements))

    # board.saveData(listInformation)

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

def startDB(request):
    """
        Esse método tem como objetivo iniciar o banco de dados para a aplicação
    """

    Type.objects.all().delete()

    db = Type(cod=1, nome="Coração")
    db.save()

    db = Type(cod=4, nome="XRAW_T")
    db.save()
    db = Type(cod=5, nome="YRAW_T")
    db.save()
    db = Type(cod=6, nome="ZRAW_T")
    db.save()
    db = Type(cod=7, nome="XVOLT_T")
    db.save()
    db = Type(cod=8, nome="YVOLT_T")
    db.save()
    db = Type(cod=9, nome="ZVOLT_T")
    db.save()

    db = Type(cod=10, nome="Eixo X")
    db.save()
    db = Type(cod=11, nome="Eixo Y")
    db.save()
    db = Type(cod=12, nome="Eixo Z")
    db.save()

    return HttpResponseRedirect('/board/')


