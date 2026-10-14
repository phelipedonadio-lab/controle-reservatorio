import time
import random
from colorama import Fore, Style, init

# Faz a cor voltar ao normal sozinha após cada print
init(autoreset=True)

mensagens = [
    "Nível 1: Muito Baixo (CRÍTICO)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito Alto (ALERTA)"
]

# Quantidade de leituras exibidas na simulação
TOTAL_LEITURAS = 8


#FUNÇÕES
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED       # crítico
    elif nivel == 2:
        return Fore.YELLOW    # atenção
    elif nivel == 3:
        return Fore.GREEN     # normal
    elif nivel == 4:
        return Fore.CYAN      # alto
    else:
        return Fore.BLUE      # nível máximo


def montar_barra(nivel):
    return "■" * nivel + "□" * (5 - nivel)


def exibir_situacao(numero, nivel):
    cor = definir_cor(nivel)
    barra = montar_barra(nivel)
    print(f"{cor}Leitura {numero:02d} | {barra} | {mensagens[nivel - 1]}")


def monitorar(total):
    print("   MONITORAMENTO DO RESERVATÓRIO DE ÁGUA\n")

    nivel = random.randint(1, 5)  # nível inicial sorteado

    for numero in range(1, total + 1):
        exibir_situacao(numero, nivel)
        time.sleep(1)   # pausa de 1 segundo

        # A cada leitura, o nível desce 1, fica igual ou sobe 1
        variacao = random.choice([-1, 0, 1])
        nivel = nivel + variacao

        # Garante que o nível nunca saia da faixa de 1 a 5
        nivel = max(1, min(5, nivel))  # impede passar dos limites

    print("\nMonitoramento encerrado.")


#EXECUÇÃO
monitorar(TOTAL_LEITURAS)