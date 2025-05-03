
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Precificação Estética", layout="centered")

st.title("💰 Precificação para Estética")
st.markdown("Preencha os campos abaixo para calcular o preço ideal dos procedimentos com base nos custos, tempo e margem de lucro.")

# 1. Informações gerais
st.header("📋 Informações do Procedimento")
procedimento = st.text_input("Nome do procedimento", placeholder="Ex: Hidragloss")

tempo_minutos = st.number_input("⏱ Tempo de duração (em minutos)", min_value=0, step=5)

# Custos variáveis por procedimento
st.subheader("Custos variáveis por procedimento")
custo_materiais = st.number_input("💉 Custo com materiais (R$)", min_value=0.0, step=1.0, format="%.2f")
aluguel_hora = st.number_input("🏢 Aluguel da sala (por hora - R$)", min_value=0.0, step=1.0, format="%.2f")
alimentacao = st.number_input("🍽 Alimentação por atendimento (R$)", min_value=0.0, step=1.0, format="%.2f")
transporte = st.number_input("🚗 Transporte por atendimento (R$)", min_value=0.0, step=1.0, format="%.2f")
taxas_financeiras = st.number_input("💳 Impostos e taxas sobre vendas (R$)", min_value=0.0, step=1.0, format="%.2f")

# Custos fixos mensais
st.header("📦 Despesas Fixas Mensais")
valor_aluguel = st.number_input("🏠 Aluguel fixo da sala", min_value=0.0, step=10.0, format="%.2f")
despesas_gerais = st.number_input("💡 Água, luz, internet etc.", min_value=0.0, step=10.0, format="%.2f")
marketing = st.number_input("📣 Investimento mensal em marketing", min_value=0.0, step=10.0, format="%.2f")
contabilidade = st.number_input("📊 Gastos com contabilidade", min_value=0.0, step=10.0, format="%.2f")

# Capacidade de atendimento
st.header("📆 Capacidade de Atendimento")
dias_trabalho = st.slider("Dias de atendimento por semana", 1, 7, 5)
horas_por_dia = st.slider("Horas de atendimento por dia", 1, 12, 8)

# Margem e campanhas
st.header("📈 Margem de Lucro e Campanhas")
margem_desejada = st.slider("Margem de lucro desejada (%)", 0, 200, 100)
desconto_campanha = st.slider("Desconto para campanhas promocionais (%)", 0, 100, 0)

# Cálculos
atendimentos_mensais = (dias_trabalho * 4) * (horas_por_dia * 60 // tempo_minutos) if tempo_minutos > 0 else 0

custo_fixo_mensal = valor_aluguel + despesas_gerais + marketing + contabilidade
custo_fixo_procedimento = custo_fixo_mensal / atendimentos_mensais if atendimentos_mensais > 0 else 0

# Aluguel da sala por procedimento baseado em tempo
aluguel_por_procedimento = (aluguel_hora / 60) * tempo_minutos

custo_variavel_total = (
    custo_materiais + aluguel_por_procedimento + alimentacao + transporte + taxas_financeiras
)

custo_total = custo_variavel_total + custo_fixo_procedimento
preco_ideal = custo_total * (1 + margem_desejada / 100)
preco_promocional = preco_ideal * (1 - desconto_campanha / 100)

# Resultados
st.header("📊 Resultado da Precificação")
st.markdown(f"**Procedimento:** {procedimento if procedimento else '---'}")
st.markdown(f"**Atendimentos mensais estimados:** {atendimentos_mensais}")
st.markdown(f"**Custo fixo por procedimento:** R$ {custo_fixo_procedimento:.2f}")
st.markdown(f"**Custo variável por procedimento:** R$ {custo_variavel_total:.2f}")
st.markdown(f"**Custo total por procedimento:** R$ {custo_total:.2f}")
st.markdown(f"**Preço ideal com lucro:** R$ {preco_ideal:.2f}")
st.markdown(f"**Preço promocional sugerido:** R$ {preco_promocional:.2f}")

# Tabela comparativa
st.header("📋 Comparativo de Preços com Variação de Margem")
margens = [50, 100, 150, 200]
dados_comparativos = {
    "Margem (%)": margens,
    "Preço Sugerido (R$)": [round(custo_total * (1 + m / 100), 2) for m in margens]
}
tabela = pd.DataFrame(dados_comparativos)
st.table(tabela)
