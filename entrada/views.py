from django.shortcuts import render

# Lista para armazenar o número de pessoas
qtd = []

def index(request):
    total = sum(qtd)  # Total de pessoas até o momento
    message = ''
    
    # Se o formulário for submetido
    if request.method == 'POST':
        if 'qtdPessoas' in request.POST:  # Quando o formulário de adicionar pessoas é enviado
            try:
                people = int(request.POST['qtdPessoas'])
                qtd.append(people)
                message = "Número adicionado com sucesso!"
            except ValueError:
                message = "Por favor, insira um número válido."
        elif 'finalizar' in request.POST:  # Quando o formulário de finalizar contagem é enviado
            total = sum(qtd)
            qtd.clear()  # Limpa a lista para o próximo evento
            message = f"Total: {total} Pessoas Participaram do Evento. "

    return render(request, 'convidados.html', {'total': total, 'message': message})
