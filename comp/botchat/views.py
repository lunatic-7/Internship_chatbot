from django.shortcuts import render
from .open_ai import generate_summary, generate_toc, generate_questions

def chatbot(request):
    if request.method == 'POST':
        comprehension = request.POST['comprehension']
        no_ques = request.POST['num-questions']
        sum_l = request.POST['sum_l']
        if request.POST.get('summary'):
            output = generate_summary(comprehension, sum_l)
        elif request.POST.get('toc'):
            output = generate_toc(comprehension)
        elif request.POST.get('questions'):
            output = generate_questions(comprehension, no_ques)
        elif request.POST.get('exit'):
            return render(request, 'exit.html')
        else:
            output = ""
        return render(request, 'chatbot.html', {'output': output, 'input': comprehension})
    else:
        return render(request, 'index.html')

def chatui(request):
    return render(request, 'chatui.html')