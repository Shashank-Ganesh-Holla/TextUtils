# I have created this file - Shashank
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    purpose = ""
    params = {}

    if spaceremove == 'on':
        for ind, char in enumerate(text):
            if ind + 1 < len(text) and not (text[ind] == '' and text[ind + 1] == ''):
                analyzed += char

        text = analyzed
        purpose += 'Removed Extra Spaces '
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if removepunc == 'on':
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed += char

        text = analyzed
        purpose += 'Removed Punctuations '
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if newlineremover == 'on':
        text = text.replace(' ', '')
        analyzed = ""
        for char in text:
            if char != '' and char != '\n' and char != '\r':
                analyzed += char

        text = analyzed
        purpose += 'Removed NewLines '
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if fullcaps == 'on':
        analyzed = ""
        for char in text:
            analyzed += char.upper()

        text = analyzed
        purpose += 'Changed to UPPERCASE '
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if charcount == 'on':
        analyzed = ""
        text = text.replace(' ', '')
        for char in text:
            if char != '' and char != '\n' and char != '\r':
                analyzed += char

        analyzed = len(analyzed)
        purpose += 'Counted Characters '
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if spaceremove != 'on' and removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and charcount != 'on':
        return HttpResponse('please select any operation and try again')

    # params = {'purpose': purpose, 'analyzed_text': text}
    return render(request, 'analyze.html', params)
