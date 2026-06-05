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

# Função para analisar os ciclos:
def analisar_ciclos():
    riscos_ciclos = []
    riscos_por_area = [0, 0, 0, 0, 0]
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)
    for indice, ciclo in enumerate(dados_missao):
        temperatura = ciclo[0]
        comunicacao = ciclo[1]
        bateria = ciclo[2]
        oxigenio = ciclo[3]
        estabilidade = ciclo[4]
        status_temperatura, risco_temperatura, msg_temperatura = analisar_temperatura(temperatura)
        status_comunicacao, risco_comunicacao, msg_comunicacao = analisar_comunicacao(comunicacao)
        status_bateria, risco_bateria, msg_bateria = analisar_bateria(bateria)
        status_oxigenio, risco_oxigenio, msg_oxigenio = analisar_oxigenio(oxigenio)
        status_estabilidade, risco_estabilidade, msg_estabilidade = analisar_estabilidade(estabilidade)
        risco_total = (risco_temperatura + risco_comunicacao + risco_bateria + risco_oxigenio + risco_estabilidade)
        riscos_ciclos.append(risco_total)
        riscos_por_area[0] += risco_temperatura
        riscos_por_area[1] += risco_comunicacao
        riscos_por_area[2] += risco_bateria
        riscos_por_area[3] += risco_oxigenio
        riscos_por_area[4] += risco_estabilidade
        classificacao = classificar_ciclo(risco_total)
        recomendacao = gerar_recomendacao(risco_total)
        print()
        print(f"CICLO {indice + 1}")
        print("-" * 60)
        print(f"Temperatura: {temperatura} °C | {status_temperatura} | {msg_temperatura}")
        print(f"Comunicação: {comunicacao}% | {status_comunicacao} | {msg_comunicacao}")
        print(f"Bateria: {bateria}% | {status_bateria} | {msg_bateria}")
        print(f"Oxigênio: {oxigenio}% | {status_oxigenio} | {msg_oxigenio}")
        print(f"Estabilidade: {estabilidade}% | {status_estabilidade} | {msg_estabilidade}")
        print()
        print(f"Pontuação de risco do ciclo: {risco_total}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")
    return riscos_ciclos, riscos_por_area

# Função do relatório final:
def gerar_relatorio_final(riscos_ciclos, riscos_por_area):
    quantidade_ciclos = len(dados_missao)
    (media_temperatura, media_comunicacao, media_bateria, media_oxigenio, media_estabilidade) = calcular_medias(dados_missao)
    maior_risco = max(riscos_ciclos)
    ciclo_mais_critico = riscos_ciclos.index(maior_risco) + 1
    risco_medio = sum(riscos_ciclos) / quantidade_ciclos
    quantidade_ciclos_criticos = 0
    for risco in riscos_ciclos:
        if risco >= 6:
            quantidade_ciclos_criticos += 1
    tendencia = analisar_tendencia(riscos_ciclos)
    area_mais_afetada = identificar_area_mais_afetada(riscos_por_area, areas_monitoradas)
    classificacao_final = classificar_ciclo(risco_medio)
    # Gerando o relatório:
    print()
    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print()
    print(f"Quantidade de ciclos analisados: {quantidade_ciclos}")
    print()
    print(f"Média de temperatura: {media_temperatura:.2f} °C")
    print(f"Média de comunicação: {media_comunicacao:.2f}%")
    print(f"Média de bateria: {media_bateria:.2f}%")
    print(f"Média de oxigênio: {media_oxigenio:.2f}%")
    print(f"Média de estabilidade: {media_estabilidade:.2f}%")
    print()
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {quantidade_ciclos_criticos}")
    print()
    print("Tendência da missão:")
    print(tendencia)
    print()
    print("Pontuação acumulada por área:")
    for i in range(len(areas_monitoradas)):
        print(f"{areas_monitoradas[i]}: {riscos_por_area[i]} pontos")
    print()
    print("Área mais afetada:")
    print(area_mais_afetada)
    print()
    print("Classificação final da missão:")
    print(classificacao_final)
    print()
    print("Conclusão:")
    if classificacao_final == "MISSÃO ESTÁVEL":
        print("A missão manteve bons indicadores operacionais e pode seguir em monitoramento padrão.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("A missão apresentou sinais de instabilidade e a equipe deve manter o plano de contingência ativo.")
    else:
        print("A missão apresentou alto risco operacional e exige intervenção imediata da equipe de controle.")

# Dados principais do projeto:
nome_missao = "Orion Test Alpha"
nome_equipe = "Equipe Apollo"
dados_missao = gerar_dados_missao(6)
areas_monitoradas = ["Temperatura interna", "Comunicação com a base", "Sistema de energia", "Suporte de oxigênio", "Estabilidade operacional"]

# Execução do código:
riscos_ciclos, riscos_por_area = analisar_ciclos()
gerar_relatorio_final(riscos_ciclos, riscos_por_area)