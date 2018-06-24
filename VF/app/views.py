# from django.shortcuts import render
# from django.utils import timezone
# from .models import Jogada
# from .forms import JogadaForm
# from .campo_minado_negocio import CampoMinado

# COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
# JOGADA_SEGURA = "Jogada Segura"
# GAME_OVER = "Game Over"
# VITORIA = "Parabéns você venceu"

# """ 
#     1. Menu para iniciar o jogo
#     2. Menu declara jogada
#     3. Regra pra vitória
    
#     4. Salvar jogadas
#     5. Continuar jogo 
#  """
# objeto = CampoMinado()

# def post_list(request):
#     if request.method == "POST":
#         form = JogadaForm(request.POST)
#         if form.is_valid():
#             jogada = form.save(commit=False)
#             jogada.created_date = timezone.now()
#             jogada.save()
#     else:
#         form = JogadaForm()

#     jogadas = Jogada.objects.all()

#     return render(request, 'app/post_list.html', {'form': form, 'jogadas':jogadas})


# def menu_inicial(objeto):
#     print("---------------------------------------")
#     print("------------ Campo Minado -------------")
#     print("---------------------------------------")
#     print("\n")
#     print(" Selecione uma opção")
#     print("1. Criar novo jogo")
#     if objeto.jogo_incompleto() == True:
#         print("2. Continuar jogo anterior")
#     print("9. Sair do Jogo")

# def iniciar_novo_jogo(contexto):

#     objeto = contexto.get(INSTANCIA)
#     objeto.criar_novo_jogo(4,4)
#     objeto.imprimir_tabuleiro()

#     return efetuar_nova_jogada(contexto)

# def continuar_jogo(contexto):
#     pass

# def efetuar_nova_jogada(contexto):

#     objeto = contexto.get(INSTANCIA)

#     while objeto.jogadas_restantes > 0:
#         linha = int(input("Defina uma linha: "))
#         coluna = int(input("Defina uma coluna: "))
#         if objeto.jogada(linha,coluna) == GAME_OVER:
#             return GAME_OVER
#         objeto.imprimir_tabuleiro()
    
#     return VITORIA

# def sair(contexto):
#     sys.exit(0)

# if __name__ == "__main__":

#     switcher = {
#         1: iniciar_novo_jogo,
#         2: continuar_jogo,
#         9: sair,
#     }

#     objeto = CampoMinado()
#     contexto = {INSTANCIA: objeto}
    
#     while True:
#         menu_inicial(objeto)
#         opcao = int(input("Opção escolhida: "))

#         func = switcher.get(opcao)

from django.shortcuts import render
from .campo_minado_negocio import CampoMinado
from .forms import JogadaForm
from .models import Jogada

VITORIA = "Parabéns!"
COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
FIM_JOGO = "Game Over"

objeto = CampoMinado()

def iniciar(request):
    jogo = JogadaForm(request.POST)
    return render(request, 'app/inicio.html', {'entrada': jogo})


def jogada(request):
    global objeto
    if request.method == 'POST':
        entrada = JogadaForm(request.POST)
        if entrada.is_valid():
            linha = entrada.cleaned_data['linha']
            coluna = entrada.cleaned_data['coluna']
            objeto = CampoMinado()
            objeto.criar_novo_jogo(linha, coluna)
            matriz = objeto.retornar_matriz()
    else:
        entrada = JogadaForm()

    mensagem = ''
    return render(request, 'app/matriz.html', {'entrada': entrada, 'matriz': matriz, 'mensagem': mensagem})


def main(request):
    global objeto
    if request.method == 'POST':
        entrada = JogadaForm(request.POST)
        if entrada.is_valid():
            linha = entrada.cleaned_data['linha']
            coluna = entrada.cleaned_data['coluna']
            mensagem = objeto.jogada(linha - 1, coluna - 1)
            jogadas_restantes = objeto.jogadas_restantes
            if mensagem == VITORIA:
                print("VITORIA ?")
                if jogadas_restantes == 0:
                    print("VITORIA!")
                    matriz = objeto.retornar_matriz
                    return render(request, 'app/fim.html', {'matriz': matriz, 'mensagem': mensagem})
            elif mensagem == COORDENADAS_INVALIDAS:
                print("COORDENADAS_INVALIDAS")
                matriz = objeto.retornar_matriz
                return render(request, 'app/matriz.html',
                              {'entrada': entrada, 'matriz': matriz, 'mensagem': mensagem})
            elif mensagem == FIM_JOGO:
                print("FIM_JOGO")
                matriz = objeto.retornar_matriz
                return render(request, 'app/fim.html', {'matriz': matriz, 'mensagem': mensagem})
            else:
                print("JOGADA")
                matriz = objeto.retornar_matriz
                return render(request, 'app/matriz.html',
{'entrada': entrada, 'matriz': matriz, 'mensagem': mensagem})