from django.shortcuts import render
from django.views.generic import DetailView
from Keirsi import *
from motivation import *
from Tomas import *
def questions(Test, constant_str):
    list_of_responses = []
    file = open(Test, 'r', encoding="utf-8")
    l = ""
    constant = 0
    for line in file:
        l += line
        constant += 1
        if constant == constant_str:
            list_of_responses.append(l)
            l = ''
            constant = 0
    return list_of_responses

def Keirsi_main(request):
    return render(request, 'keirsi/Keirsi.html')

def Keirsi_questions(request):
    return render(request, 'keirsi/questions.html', {'questions': questions("тест Кейрси (вопросы).txt", 3)})

def Keirsi_answer(request):
    if request.method == 'POST':
        answers = []
        for key in request.POST:
            if key.startswith('question'):
                answers.append(request.POST[key])
        if len(answers) == 70:
            answers = Keirsi(answers)
        else:
            answers = "вы заполнили не все данные"
        return render(request, 'keirsi/answer.html', {'answers': answers})

def motivation_main(request):
    return render(request, 'motivation/motivation.html')

def motivation_questions(request):
    return render(request, 'motivation/questions.html', {'questions': questions("тест Мотивационный (вопросы).txt", 6)})

def motivation_answer(request):
    if request.method == 'POST':
        answers = []
        for key in request.POST:
            if key.startswith('question'):
                answers.append(request.POST[key])
        if len(answers) == 14:
            answers = motivation(answers)
        else:
            answers = "вы заполнили не все данные"
        return render(request, 'motivation/answer.html', {'answers': answers})
    

def Tomas_main(request):
    return render(request, 'Tomas/Tomas.html')

def Tomas_questions(request):
    return render(request, 'Tomas/questions.html', {'questions': questions("тест Томаса (вопросы).txt", 2)})

def Tomas_answer(request):
    if request.method == 'POST':
        answers = []
        for key in request.POST:
            if key.startswith('question'):
                answers.append(request.POST[key])
        if len(answers) == 30:
            answers = Tomas(answers)
        else:
            answers = "вы заполнили не все данные"
        return render(request, 'Tomas/answer.html', {'answers': answers})
