import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

mensagens = [
    "Nível 1: Muito Baixo (CRÍTICO)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito Alto (ALERTA)"
]

TOTAL_LEITURAS = 8


def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE


def montar_barra(nivel):
    return "█" * nivel + "░" * (5 - nivel)


def exibir_situacao(numero, nivel):
    cor = definir_cor(nivel)
    barra = montar_barra(nivel)
    print(f"{cor}Leitura {numero:02d} | {barra} | {mensagens[nivel - 1]}")


def monitorar(total):
    print("   MONITORAMENTO DO RESERVATÓRIO DE ÁGUA\n")

    nivel = random.randint(1, 5)  # nível inicial sorteado

    for numero in range(1, total + 1):
        exibir_situacao(numero, nivel)
        time.sleep(1)

        variacao = random.choice([-1, 0, 1])
        nivel = nivel + variacao
        nivel = max(1, min(5, nivel))  # impede passar dos limites

    print("\nMonitoramento encerrado.")


monitorar(TOTAL_LEITURAS)