# 💧🚨 Monitoramento de Reservatório de Água
 
![Python](https://skillicons.dev/icons?i=python) ![VS Code](https://skillicons.dev/icons?i=vscode)
 
![Nível](https://img.shields.io/badge/Nível-Iniciante-yellow?style=for-the-badge)
 
---
 
## 📑 Sumário
 
- [💧🚨 Monitoramento de Reservatório de Água](#-monitoramento-de-reservatório-de-água)
  - [📑 Sumário](#-sumário)
  - [Descrição](#descrição)
  - [Objetivo do Projeto](#objetivo-do-projeto)
  - [▶️ Como Executar](#️-como-executar)
  - [Instruções de Uso](#instruções-de-uso)
  - [📋 Tabela de Níveis do Reservatório](#-tabela-de-níveis-do-reservatório)
  - [🧩 Estrutura do Código](#-estrutura-do-código)
  - [⚙️ Personalização](#️-personalização)
  - [💬 Exemplo de Execução](#-exemplo-de-execução)
---
 
## Descrição
 
Sistema simples, executado no **terminal** (a tela de texto onde o programa mostra suas mensagens), que **simula o monitoramento do nível de água de um reservatório**.
 
A cada segundo, o programa faz uma nova "leitura" do reservatório e exibe a situação atual com uma **cor**, uma **barra visual** e uma **mensagem de alerta**, seguindo a progressão de risco: do nível crítico (muito baixo) até o alerta de nível máximo.
 
As leituras são geradas de forma **aleatória**, mas com variação realista: o nível sobe 1, desce 1 ou permanece igual, sem saltos bruscos, como em um reservatório de verdade.
 
---
 
## Objetivo do Projeto
 
Praticar conceitos fundamentais de programação, como:
 
- 📚 Listas (`mensagens`)
- 🧩 Funções (`definir_cor`, `montar_barra`, `exibir_situacao`, `monitorar`)
- 🔀 Estrutura de decisão (`if` / `elif` / `else`)
- 🔁 Estrutura de repetição (`for` com `range`)
- 🎲 Geração de números aleatórios (biblioteca `random`)
- ⏱️ Pausas no programa (biblioteca `time`)
- 🎨 Cores no terminal (biblioteca `colorama`)
- 🔤 Textos formatados (f-strings, que são textos com `{variáveis}` dentro)
---
 
## ▶️ Como Executar
 
1. Instale a biblioteca de cores (só na primeira vez):
```bash
pip install colorama
```
 
2. Execute o programa:
```bash
python app.py
```
 
> [!NOTE]
> Requer Python 3.6 ou superior, pois o programa usa f-strings.
 
> [!WARNING]
> Se aparecer o erro `ModuleNotFoundError: No module named 'colorama'`, a biblioteca foi instalada em um Python diferente do que está rodando o programa. No VS Code, aperte `Ctrl + Shift + P`, escolha **Python: Select Interpreter** e selecione o mesmo Python usado na instalação.
 
---
 
## Instruções de Uso
 
1. Execute o arquivo `app.py`.
2. Não é preciso digitar nada: o programa **simula** as leituras sozinho.
3. O programa sorteia um nível inicial (de 1 a 5) e exibe **8 leituras**, uma por segundo.
4. A cada leitura, o nível pode **subir 1, descer 1 ou ficar igual**.
5. Ao final, o programa exibe "Monitoramento encerrado." e o terminal volta ao estilo normal.
> [!TIP]
> Como as leituras são sorteadas, cada execução gera uma sequência diferente.
 
---
 
## 📋 Tabela de Níveis do Reservatório
 
Cada nível tem uma situação, uma cor e uma barra própria:
 
| Nível | Situação              | Cor      | Barra   |
| ----- | --------------------- | -------- | ------- |
| 1     | Muito baixo (CRÍTICO) | Vermelho | `█░░░░` |
| 2     | Baixo                 | Amarelo  | `██░░░` |
| 3     | Médio                 | Verde    | `███░░` |
| 4     | Alto                  | Ciano    | `████░` |
| 5     | Muito alto (ALERTA)   | Azul     | `█████` |
 
> [!NOTE]
> A aparência exata das cores depende do tema do terminal. O azul, por exemplo, pode aparecer com tom de violeta. Se isso acontecer, troque `Fore.BLUE` por `Fore.LIGHTBLUE_EX` na função `definir_cor`.
 
---
 
## 🧩 Estrutura do Código
 
| Parte                 | Tipo      | O que faz                                                                         |
| --------------------- | --------- | --------------------------------------------------------------------------------- |
| `mensagens`           | Lista     | Guarda a mensagem de cada nível (nível 1 na posição 0, nível 5 na posição 4)      |
| `TOTAL_LEITURAS`      | Constante | Define quantas leituras serão exibidas (valor fixo, por isso em maiúsculas)       |
| `definir_cor(nivel)`  | Função    | Recebe o nível e devolve a cor correspondente                                     |
| `montar_barra(nivel)` | Função    | Monta a barra visual repetindo `█` (preenchido) e `░` (vazio)                     |
| `exibir_situacao()`   | Função    | Junta cor, barra e mensagem e mostra a leitura na tela                            |
| `monitorar(total)`    | Função    | Controla a simulação: sorteia o nível inicial, repete as leituras e varia o nível |
 
**Detalhes que merecem atenção:**
 
- `init(autoreset=True)` faz a cor voltar ao normal sozinha depois de cada `print`, evitando que a cor "vaze" para outras linhas.
- `random.choice([-1, 0, 1])` sorteia se o nível desce, fica igual ou sobe.
- `max(1, min(5, nivel))` "prende" o nível entre 1 e 5: se der 6 vira 5, se der 0 vira 1.
- `time.sleep(1)` faz o programa esperar 1 segundo entre as leituras.
---
 
## ⚙️ Personalização
 
Você pode ajustar o programa mudando poucas linhas:
 
| O que mudar                      | Onde                             | Exemplo                                         |
| -------------------------------- | -------------------------------- | ----------------------------------------------- |
| Quantidade de leituras           | `TOTAL_LEITURAS`                 | `TOTAL_LEITURAS = 20`                           |
| Velocidade do monitoramento      | `time.sleep(...)` em `monitorar` | `time.sleep(0.5)` para meio segundo             |
| Cores de cada nível              | função `definir_cor`             | `return Fore.LIGHTBLUE_EX`                      |
| Textos das mensagens             | lista `mensagens`                | `"Nível 1: Reservatório quase vazio!"`          |
| Repetir sempre a mesma sequência | topo do arquivo                  | adicionar `random.seed(42)` depois dos `import` |
 
---
 
## 💬 Exemplo de Execução
 
<details>
<summary>Clique para ver um exemplo de saída</summary>

```
   MONITORAMENTO DO RESERVATÓRIO DE ÁGUA

Leitura 01 | ███░░ | Nível 3: Médio
Leitura 02 | ███░░ | Nível 3: Médio
Leitura 03 | ██░░░ | Nível 2: Baixo
Leitura 04 | █░░░░ | Nível 1: Muito Baixo (CRÍTICO)
Leitura 05 | █░░░░ | Nível 1: Muito Baixo (CRÍTICO)
Leitura 06 | ██░░░ | Nível 2: Baixo
Leitura 07 | ███░░ | Nível 3: Médio
Leitura 08 | ████░ | Nível 4: Alto

Monitoramento encerrado.
```

> No terminal, cada linha aparece com a cor do seu nível. Como as leituras são aleatórias, a sua sequência será diferente.

</details>
