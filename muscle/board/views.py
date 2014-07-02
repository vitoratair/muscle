# coding: utf-8
from django.shortcuts import render
from muscle.board.library.readData import ReadData


def search(request):
    """
        Esse método tem como objetivo a busca das informações na placa
    """
    byte = 1
    listInformation = []
    board = ReadData()
    data = board.getStart()

    for elements in data:
        if len(elements) != 0:
            listInformation.append(board.execParser(elements))

    board.saveData(listInformation)

    return render(request, 'board/search.html')







