
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Calculadora de Precificação", layout="centered")

st.title("🧮 Calculadora de Precificação de Procedimentos")

st.header("1️⃣ Informações Gerais")

# Custo com insumos por procedimento
valor_insumo = st.number_input("Custo com insumos (por procedimento)", min_value=0.0, format="%.2f")
st.markdown("""
**Exemplo:** Se o custo dos materiais utilizados para realizar um procedimento é R$ 20,00, insira 20,00.
""")

# Aluguel da sala por hora
valor_sala = st.number_input("Aluguel da sala por hora", min_value=0.0, format="%.2f")
st.markdown("""
**Exemplo:** Se você aluga a sala por R$ 100,00 a cada 2 horas de atendimento, insira 50,00 por hora.
""")

# Duração do procedimento em horas
tempo_procedimento = st.number_input("Duração do procedimento (em horas)", min_value=0.1, format="%.2f")
st.markdown("""
**Exemplo:** Se o procedimento leva 1,5 horas, insira 1,5.
""")

# Quantidade de atendimentos por dia
qtd_atendimentos_dia = st.number_input("Quantidade média de atendimentos por dia", min_value=1, value=1)
st.markdown("""
**Exemplo:** Se você realiza 10 atendimentos por dia, insira 10.
""")

# Gasto diário com transporte
transporte_dia = st.number_input("Gasto diário com transporte", min_value=0.0, format="%.2f")
st.markdown("""
**Exemplo:** Se o gasto diário com transporte é de R$ 30,00, insira 30,00.
""")

# Gasto diário com alimentação
alimentacao_dia = st.number_input("Gasto diário com alimentação", min_value=0.0, format="%.2f")
st.markdown("""
**Exemplo:** Se o gasto diário com alimentação é de R$ 20,00, insira 20,00.
""")

# Taxa de vendas (cartão, marketplace etc.)
taxa_cartao = st.number_input("Taxas com vendas (cartão, marketplaces etc.) (%)", min_value=0.0, max_value=100.0, format="%.2f")
st.markdown("""
**Exemplo:** Se a taxa de vendas for de 5%, insira 5.
""")

# Impostos sobre a venda
impostos_percentual = st.number_input("Impostos sobre a venda (%)", min_value=0.0, max_value=100.0, format="%.2f")
st.markdown("""
**Exemplo:** Se os impostos sobre o valor da venda forem 15%, insira 15.
""")

st.header("2️⃣ Despesas Fixas")

# Gastos com marketing mensal
despesa_marketing = st.number_input("Gastos com marketing (mensal)", min_value=0.0, format="%.2f")
st.markdown("""
**Exemplo:** Se seus gastos com marketing são R$ 2.000,00 mensais, insira 2000.
""")

# Gastos com contabilidade mensal
despesa_contador = st.number_input("Gastos com contabilidade (mensal)", min_value=0.0, format="%.2f")
st.markdown("""
**Exemplo:** Se você paga R$ 500,00 por mês em contabilidade, insira 500.
""")

# Outras despesas fixas
outros_fixos = st.number_input("Outras despesas fixas (mensal)", min_value=0.0, format="%.2f")
st.markdown("""
**Exemplo:** Se você tem outras despesas fixas de R$ 1.000,00 mensais, insira 1000.
""")

# Dias trabalhados por mês
dias_trabalho_mes = st.number_input("Dias trabalhados por mês", min_value=1, max_value=31, value=20)
st.markdown("""
**Exemplo:** Se você trabalha 20 dias por mês, insira 20.
""")

st.header("3️⃣ Lucro e Descontos")

# Margem de lucro desejada
margem_desejada = st.number_input("Margem de lucro desejada (%)", min_value=0.0, max_value=100.0, format="%.2f")
st.markdown("""
**Exemplo:** Se você deseja ter uma margem de lucro de 30%, insira 30.
""")

# Desconto promocional
desconto_campanha = st.number_input("Desconto promocional (%)", min_value=0.0, max_value=100.0, format="%.2f")
st.markdown("""
**Exemplo:** Se você deseja oferecer 10% de desconto, insira 10.
""")

# Cálculos
custo_sala = valor_sala * tempo_procedimento
custo_transporte = transporte_dia / qtd_atendimentos_dia
custo_alimentacao = alimentacao_dia / qtd_atendimentos_dia

custo_total_variavel = valor_insumo + custo_sala + custo_transporte + custo_alimentacao
custo_fixo_por_procedimento = (despesa_marketing + despesa_contador + outros_fixos) / (dias_trabalho_mes * qtd_atendimentos_dia)
custo_total = custo_total_variavel + custo_fixo_por_procedimento

preco_sugerido = custo_total / (1 - (taxa_cartao + impostos_percentual + margem_desejada) / 100)
preco_com_desconto = preco_sugerido * (1 - desconto_campanha / 100)

lucro = preco_sugerido - custo_total - (preco_sugerido * (taxa_cartao + impostos_percentual) / 100)
lucro_desconto = preco_com_desconto - custo_total - (preco_com_desconto * (taxa_cartao + impostos_percentual) / 100)

# Exibição dos resultados
st.header("4️⃣ Resultado")

col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Sem Desconto")
    st.write(f"Preço sugerido: R$ {preco_sugerido:.2f}")
    st.write(f"Lucro estimado: R$ {lucro:.2f}")

with col2:
    st.subheader("🎯 Com Desconto")
    st.write(f"Preço com desconto: R$ {preco_com_desconto:.2f}")
    st.write(f"Lucro com desconto: R$ {lucro_desconto:.2f}")

# Detalhamento dos cálculos
if st.button("Ver detalhamento dos cálculos"):
    st.subheader("🔍 Detalhamento do Cálculo")
    st.write(f"**Custo com insumos:** R$ {valor_insumo:.2f}")
    st.write(f"**Custo com sala:** R$ {custo_sala:.2f}")
    st.write(f"**Custo com transporte (por atendimento):** R$ {custo_transporte:.2f}")
    st.write(f"**Custo com alimentação (por atendimento):** R$ {custo_alimentacao:.2f}")
    st.write(f"**Custo total variável:** R$ {custo_total_variavel:.2f}")
    st.write(f"**Custo fixo por procedimento:** R$ {custo_fixo_por_procedimento:.2f}")
    st.write(f"**Custo total:** R$ {custo_total:.2f}")
    st.write(f"**Preço sugerido sem desconto:** R$ {preco_sugerido:.2f}")
    st.write(f"**Preço com desconto:** R$ {preco_com_desconto:.2f}")
    st.write(f"**Lucro sem desconto:** R$ {lucro:.2f}")
    st.write(f"**Lucro com desconto:** R$ {lucro_desconto:.2f}")

# Gráfico
st.subheader("📊 Comparativo Visual")

fig, ax = plt.subplots()
labels = ['Preço', 'Custo', 'Lucro']
sem_desconto = [preco_sugerido, custo_total, lucro]
com_desconto = [preco_com_desconto, custo_total, lucro_desconto]

x = range(len(labels))
ax.bar([p - 0.15 for p in x], sem_desconto, width=0.3, label='Sem Desconto')
ax.bar([p + 0.15 for p in x], com_desconto, width=0.3, label='Com Desconto')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel("Valor (R$)")
ax.legend()
st.pyplot(fig)