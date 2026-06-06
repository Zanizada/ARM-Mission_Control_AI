"""
MISSION CONTROL AI - Versão adaptada para GS de SERS
Tema: Monitoramento inteligente de missão espacial com foco em energia renovável,
sustentabilidade, alertas automáticos e tomada de decisão básica.

Observação importante:
A matriz principal dados_missao continua seguindo exatamente o modelo da GS de Python:
[temperatura, comunicacao, bateria, oxigenio, estabilidade]

Para atender à GS de SERS, a coluna "bateria" é tratada como parte do
Sistema de Energia da missão. A partir dela, o programa calcula energia armazenada,
geração solar estimada, consumo operacional estimado, saldo energético e eficiência.
"""

import random

"""
Constantes usadas na análise energética da GS de SERS.
Esses valores são simulados e servem para transformar a porcentagem de bateria
em indicadores mais ligados a energia, potência e sustentabilidade.
"""
CAPACIDADE_BATERIA_KWH = 500   # Capacidade máxima estimada do banco de baterias da missão
POTENCIA_SOLAR_MAX_KW = 80     # Potência máxima estimada dos painéis solares
CONSUMO_BASE_KW = 45           # Consumo médio base dos módulos essenciais
DURACAO_CICLO_HORAS = 1        # Cada ciclo representa 1 hora simulada da missão

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
    return dados

# Funções de análise individual:
def analisar_temperatura(temperatura):
    if temperatura < 18:
        return "ATENÇÃO", 1, "Temperatura muito baixa. Verificar controle térmico."
    elif temperatura <= 30:
        return "NORMAL", 0, "Temperatura estável."
    elif temperatura <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada. Monitorar resfriamento."
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento. Acionar controle térmico."

def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico."
    elif comunicacao < 60:
        return "ATENÇÃO", 1, "Comunicação instável. Reforçar tentativa de contato."
    else:
        return "NORMAL", 0, "Comunicação estável."


def calcular_dados_energeticos(temperatura, comunicacao, bateria, estabilidade):
    """
    Calcula indicadores energéticos simulados para atender à GS de SERS.
    A ideia é representar uma missão abastecida por energia renovável,
    principalmente geração solar. O cálculo considera:
    - energia armazenada na bateria;
    - geração solar estimada no ciclo;
    - consumo operacional estimado;
    - saldo energético;
    - eficiência energética.
    Esses cálculos são simulações simples, feitas apenas com lógica de programação.
    """
    # Energia armazenada com base na porcentagem de bateria.
    energia_armazenada_kwh = (bateria / 100) * CAPACIDADE_BATERIA_KWH
    # Temperaturas muito altas ou muito baixas reduzem a eficiência do sistema energético.
    if temperatura > 35:
        fator_temperatura = 0.85
    elif temperatura > 30:
        fator_temperatura = 0.92
    elif temperatura < 18:
        fator_temperatura = 0.90
    else:
        fator_temperatura = 1.00
    # A estabilidade operacional influencia a capacidade de geração e distribuição de energia.
    fator_estabilidade = estabilidade / 100
    # Geração solar estimada no ciclo.
    geracao_solar_kwh = (
        POTENCIA_SOLAR_MAX_KW
        * DURACAO_CICLO_HORAS
        * fator_temperatura
        * fator_estabilidade
    )
    # Consumo base dos módulos essenciais.
    consumo_operacional_kwh = CONSUMO_BASE_KW * DURACAO_CICLO_HORAS
    # Sistemas em dificuldade exigem energia extra para correção, redundância ou contingência.
    if comunicacao < 60:
        consumo_operacional_kwh += 5
    if estabilidade < 70:
        consumo_operacional_kwh += 8
    if temperatura > 30 or temperatura < 18:
        consumo_operacional_kwh += 6
    # Saldo positivo significa que a geração renovável cobriu o consumo do ciclo.
    # Saldo negativo significa que a missão consumiu mais do que gerou.
    saldo_energetico_kwh = geracao_solar_kwh - consumo_operacional_kwh
    # Eficiência simulada: quanto da demanda foi coberta pela geração renovável.
    eficiencia_energetica = (geracao_solar_kwh / consumo_operacional_kwh) * 100
    return {
        "energia_armazenada_kwh": energia_armazenada_kwh,
        "geracao_solar_kwh": geracao_solar_kwh,
        "consumo_operacional_kwh": consumo_operacional_kwh,
        "saldo_energetico_kwh": saldo_energetico_kwh,
        "eficiencia_energetica": eficiencia_energetica
    }

def analisar_energia(bateria, dados_energia):
    """
    Analisa o sistema de energia da missão.
    Para a GS de Python, a bateria continua sendo a terceira coluna da matriz.
    Para a GS de SERS, a análise fica mais completa porque também considera:
    geração solar, consumo operacional, saldo energético e eficiência.
    """
    saldo = dados_energia["saldo_energetico_kwh"]
    eficiencia = dados_energia["eficiencia_energetica"]
    if bateria < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico. Ativar modo de economia de energia."
    elif saldo < -15:
        return "CRÍTICO", 2, "Consumo maior que a geração renovável. Reduzir módulos não essenciais."
    elif bateria < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado. Priorizar recarga e economia."
    elif saldo < 0:
        return "ATENÇÃO", 1, "Saldo energético negativo. Monitorar geração solar."
    elif eficiencia < 80:
        return "ATENÇÃO", 1, "Eficiência energética abaixo do ideal."
    else:
        return "NORMAL", 0, "Energia renovável suficiente e sistema energético estável."

def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico. Acionar suporte à vida."
    elif oxigenio < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal. Reduzir consumo interno."
    else:
        return "NORMAL", 0, "Oxigênio adequado."

def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica."
    elif estabilidade < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida."
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada."

# Funções de classificação geral:
def classificar_ciclo(risco_total):
    if risco_total <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco_total <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(analises, dados_energia):
    risco_total = sum(analise["risco"] for analise in analises)
    temperatura = analises[0]
    comunicacao = analises[1]
    energia = analises[2]
    oxigenio = analises[3]
    estabilidade = analises[4]
    if risco_total <= 2:
        return "Manter operação normal, seguir monitoramento e conservar energia renovável."
    # Recomendações para casos críticos, priorizando segurança e sustentabilidade.
    if energia["risco"] == 2:
        return "Ativar modo de economia, priorizar painéis solares e desligar módulos não essenciais."
    if oxigenio["risco"] == 2:
        return "Acionar protocolo de suporte à vida e reduzir consumo dos sistemas internos."
    if temperatura["risco"] == 2:
        return "Acionar controle térmico e reduzir carga energética dos módulos aquecidos."
    if comunicacao["risco"] == 2:
        return "Reorientar antenas, tentar restabelecer contato e manter registro local dos dados."
    if estabilidade["risco"] == 2:
        return "Ativar modo de segurança e reduzir operações não essenciais."
    # Recomendações para casos de atenção.
    if dados_energia["saldo_energetico_kwh"] < 0:
        return "Monitorar consumo, reduzir desperdício energético e preparar plano de contingência."
    return "Monitorar sistemas em atenção e preparar plano de contingência."

def analisar_tendencia(riscos_ciclos):
    primeiro_risco = riscos_ciclos[0]
    ultimo_risco = riscos_ciclos[-1]
    if ultimo_risco > primeiro_risco:
        return "A missão apresentou tendência de piora."
    elif ultimo_risco < primeiro_risco:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."

def identificar_area_mais_afetada(riscos_por_area):
    maior_risco = max(riscos_por_area)
    indice_maior_risco = riscos_por_area.index(maior_risco)
    return areas_monitoradas[indice_maior_risco]

# Funções de cálculo do relatório:
def calcular_medias(dados):
    quantidade_ciclos = len(dados)
    soma_temperatura = 0
    soma_comunicacao = 0
    soma_bateria = 0
    soma_oxigenio = 0
    soma_estabilidade = 0
    for ciclo in dados:
        soma_temperatura += ciclo[0]
        soma_comunicacao += ciclo[1]
        soma_bateria += ciclo[2]
        soma_oxigenio += ciclo[3]
        soma_estabilidade += ciclo[4]
    return (soma_temperatura / quantidade_ciclos, soma_comunicacao / quantidade_ciclos, soma_bateria / quantidade_ciclos, soma_oxigenio / quantidade_ciclos, soma_estabilidade / quantidade_ciclos)

def calcular_resumo_energetico(historico_energia):
    """
    Calcula médias e totais dos indicadores energéticos da GS de SERS.
    """
    quantidade_ciclos = len(historico_energia)
    total_energia_armazenada = 0
    total_geracao_solar = 0
    total_consumo = 0
    total_saldo = 0
    total_eficiencia = 0
    for dados in historico_energia:
        total_energia_armazenada += dados["energia_armazenada_kwh"]
        total_geracao_solar += dados["geracao_solar_kwh"]
        total_consumo += dados["consumo_operacional_kwh"]
        total_saldo += dados["saldo_energetico_kwh"]
        total_eficiencia += dados["eficiencia_energetica"]
    return {"media_energia_armazenada": total_energia_armazenada / quantidade_ciclos, "total_geracao_solar": total_geracao_solar, "total_consumo": total_consumo, "total_saldo": total_saldo, "media_eficiencia": total_eficiencia / quantidade_ciclos}

# Função para analisar os ciclos:
def analisar_ciclos():
    riscos_ciclos = []
    riscos_por_area = [0, 0, 0, 0, 0]
    historico_energia = []
    print("=" * 60)
    print("MISSION CONTROL AI - SERS")
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
        dados_energia = calcular_dados_energeticos(temperatura, comunicacao, bateria, estabilidade)
        historico_energia.append(dados_energia)
        status_temperatura, risco_temperatura, msg_temperatura = analisar_temperatura(temperatura)
        status_comunicacao, risco_comunicacao, msg_comunicacao = analisar_comunicacao(comunicacao)
        status_energia, risco_energia, msg_energia = analisar_energia(bateria, dados_energia)
        status_oxigenio, risco_oxigenio, msg_oxigenio = analisar_oxigenio(oxigenio)
        status_estabilidade, risco_estabilidade, msg_estabilidade = analisar_estabilidade(estabilidade)
        analises = [
            {"area": "Temperatura", "status": status_temperatura, "risco": risco_temperatura, "mensagem": msg_temperatura},
            {"area": "Comunicação", "status": status_comunicacao, "risco": risco_comunicacao, "mensagem": msg_comunicacao},
            {"area": "Energia", "status": status_energia, "risco": risco_energia, "mensagem": msg_energia},
            {"area": "Oxigênio", "status": status_oxigenio, "risco": risco_oxigenio, "mensagem": msg_oxigenio},
            {"area": "Estabilidade", "status": status_estabilidade, "risco": risco_estabilidade, "mensagem": msg_estabilidade}
        ]
        risco_total = sum(analise["risco"] for analise in analises)
        riscos_ciclos.append(risco_total)
        for i in range(len(analises)):
            riscos_por_area[i] += analises[i]["risco"]
        classificacao = classificar_ciclo(risco_total)
        recomendacao = gerar_recomendacao(analises, dados_energia)
        print()
        print(f"CICLO {indice + 1}")
        print("-" * 60)
        print(f"Temperatura: {temperatura} °C | {status_temperatura} | {msg_temperatura}")
        print(f"Comunicação: {comunicacao}% | {status_comunicacao} | {msg_comunicacao}")
        print(f"Energia/Bateria: {bateria}% | {status_energia} | {msg_energia}")
        print(f"Oxigênio: {oxigenio}% | {status_oxigenio} | {msg_oxigenio}")
        print(f"Estabilidade: {estabilidade}% | {status_estabilidade} | {msg_estabilidade}")
        print()
        print("Indicadores energéticos simulados:")
        print(f"Energia armazenada: {dados_energia['energia_armazenada_kwh']:.2f} kWh")
        print(f"Geração solar estimada: {dados_energia['geracao_solar_kwh']:.2f} kWh")
        print(f"Consumo operacional estimado: {dados_energia['consumo_operacional_kwh']:.2f} kWh")
        print(f"Saldo energético: {dados_energia['saldo_energetico_kwh']:.2f} kWh")
        print(f"Eficiência energética: {dados_energia['eficiencia_energetica']:.2f}%")
        print()
        print(f"Pontuação de risco do ciclo: {risco_total}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")
    return riscos_ciclos, riscos_por_area, historico_energia

# Função do relatório final:
def gerar_relatorio_final(riscos_ciclos, riscos_por_area, historico_energia):
    quantidade_ciclos = len(dados_missao)
    (media_temperatura, media_comunicacao, media_bateria, media_oxigenio, media_estabilidade) = calcular_medias(dados_missao)
    resumo_energia = calcular_resumo_energetico(historico_energia)
    maior_risco = max(riscos_ciclos)
    ciclo_mais_critico = riscos_ciclos.index(maior_risco) + 1
    risco_medio = sum(riscos_ciclos) / quantidade_ciclos
    quantidade_ciclos_criticos = 0
    for risco in riscos_ciclos:
        if risco >= 6:
            quantidade_ciclos_criticos += 1
    tendencia = analisar_tendencia(riscos_ciclos)
    area_mais_afetada = identificar_area_mais_afetada(riscos_por_area)
    classificacao_final = classificar_ciclo(risco_medio)
    print()
    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print()
    print(f"Quantidade de ciclos analisados: {quantidade_ciclos}")
    print()
    print("Médias operacionais:")
    print(f"Média de temperatura: {media_temperatura:.2f} °C")
    print(f"Média de comunicação: {media_comunicacao:.2f}%")
    print(f"Média de bateria: {media_bateria:.2f}%")
    print(f"Média de oxigênio: {media_oxigenio:.2f}%")
    print(f"Média de estabilidade: {media_estabilidade:.2f}%")
    print()
    print("Resumo energético sustentável - SERS:")
    print(f"Capacidade máxima simulada da bateria: {CAPACIDADE_BATERIA_KWH} kWh")
    print(f"Potência solar máxima simulada: {POTENCIA_SOLAR_MAX_KW} kW")
    print(f"Energia armazenada média: {resumo_energia['media_energia_armazenada']:.2f} kWh")
    print(f"Geração solar total estimada: {resumo_energia['total_geracao_solar']:.2f} kWh")
    print(f"Consumo operacional total estimado: {resumo_energia['total_consumo']:.2f} kWh")
    print(f"Saldo energético total: {resumo_energia['total_saldo']:.2f} kWh")
    print(f"Eficiência energética média: {resumo_energia['media_eficiencia']:.2f}%")
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
        print("A missão manteve bons indicadores operacionais e energéticos.")
        print("O uso de energia renovável foi suficiente para manter os módulos essenciais.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("A missão apresentou sinais de instabilidade e exige monitoramento constante.")
        print("A equipe deve reduzir desperdício energético e manter o plano de contingência ativo.")
    else:
        print("A missão apresentou alto risco operacional e energético.")
        print("É necessário ativar modo de segurança, economizar energia e priorizar suporte à vida.")
    print()
    print("Impacto sustentável da solução:")
    print("O sistema ajuda a evitar desperdício de energia, identifica falhas no sistema energético")
    print("e apoia decisões automáticas para manter a missão funcionando com recursos renováveis.")

# Dados principais do projeto:
nome_missao = "Artemis III Test Alpha"    # Nome de missão simulado
nome_equipe = "Equipe ARM"                # Nome do nosso grupo
dados_missao = gerar_dados_missao(6)
areas_monitoradas = ["Temperatura interna", "Comunicação com a base", "Sistema de energia renovável", "Suporte de oxigênio", "Estabilidade operacional"]

# Execução do código:
riscos_ciclos, riscos_por_area, historico_energia = analisar_ciclos()
gerar_relatorio_final(riscos_ciclos, riscos_por_area, historico_energia)