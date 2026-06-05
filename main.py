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

# Funções de classificação geral:
def classificar_ciclo(risco_total):
    if risco_total <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco_total <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(risco_total):
    if risco_total <= 2:
        return "Manter operação normal e continuar monitoramento."
    elif risco_total <= 5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar sistemas críticos."

def analisar_tendencia(riscos_ciclos):
    primeiro_risco = riscos_ciclos[0]
    ultimo_risco = riscos_ciclos[-1]
    if ultimo_risco > primeiro_risco:
        return "A missão apresentou tendência de piora."
    elif ultimo_risco < primeiro_risco:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."

def identificar_area_mais_afetada(riscos_por_area, areas_monitoradas):
    maior_risco = max(riscos_por_area)
    indice_maior_risco = riscos_por_area.index(maior_risco)
    return areas_monitoradas[indice_maior_risco]

def calcular_medias(dados_missao):
    quantidade_ciclos = len(dados_missao)
    soma_temperatura = 0
    soma_comunicacao = 0
    soma_bateria = 0
    soma_oxigenio = 0
    soma_estabilidade = 0
    for ciclo in dados_missao:
        soma_temperatura += ciclo[0]
        soma_comunicacao += ciclo[1]
        soma_bateria += ciclo[2]
        soma_oxigenio += ciclo[3]
        soma_estabilidade += ciclo[4]
    media_temperatura = soma_temperatura / quantidade_ciclos
    media_comunicacao = soma_comunicacao / quantidade_ciclos
    media_bateria = soma_bateria / quantidade_ciclos
    media_oxigenio = soma_oxigenio / quantidade_ciclos
    media_estabilidade = soma_estabilidade / quantidade_ciclos
    return (media_temperatura, media_comunicacao, media_bateria, media_oxigenio, media_estabilidade)