import random

# Função para gerar os dados da missão:
def gerar_dados_missao(quantidade_ciclos):
    dados = []
    for i in range(quantidade_ciclos):
        temperatura = random.randint(15, 42)
        comunicacao = random.randint(20, 100)
        bateria = random.randint(10, 100)
        oxigenio = random.randint(70, 100)
        estabilidade = random.randint(25, 100)
        ciclo = [temperatura, comunicacao, bateria, oxigenio, estabilidade]
        dados.append(ciclo)
        # [temperatura, comunicacao, bateria, oxigenio, estabilidade]
    return dados

# Funções de análise individual:
def analisar_temperatura(temperatura):
    if temperatura < 18:
        return "ATENÇÃO", 1, "Temperatura muito baixa"
    elif temperatura <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif temperatura <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"

def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif comunicacao < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"

def analisar_bateria(bateria):
    if bateria < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif bateria < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"

def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif oxigenio < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"

def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif estabilidade < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"