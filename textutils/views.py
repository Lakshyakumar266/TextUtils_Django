# Page is created By Devloper
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analize(request):
    text = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullchap = request.POST.get('fullchap', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    analized = text

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analized = ''
        for char in text:
            if char not in punctuations:
                analized = analized+char
                text = analized

    if fullchap == 'on':
        analized = ''
        for char in text:
            analized = analized + char.upper()
            text = analized

    if (newlineremove == 'on'):
        analized = ''
        for char in text:
            if char != '\n' and char != '\r':
                analized = analized + char
                text = analized

    if (extraspaceremove == 'on'):
        analized = ''
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analized = analized + char
        text = analized

    if (charcount == 'on'):
        analized = ''
        analized = f'Length Of Your Text [ \n{text}\n ] is {len(text)}'
        text = analized

    params = {"analized_text": analized}
    return render(request, 'analize.html', params)
