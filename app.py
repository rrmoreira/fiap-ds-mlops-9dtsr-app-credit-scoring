import streamlit as st
import requests
import json
import locale

def get_prediction(data):
    print(json.dumps(data))
    endpoit = st.secrets["API-ENDPOINT"]
    headers = {
        "Content-Type": "application/json",
        "x-api-key": st.secrets["API-KEY"]
    }
    response = requests.post(endpoit, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        print(result)
        
        """
            Esta análise ocorre de forma automatizada, onde um modelo de Machine Learning
            pré-treinado realiza a previsão de acordo com os dados fornecidos do cliente.
        """
                
        predicted_value = result['prediction']
        if predicted_value == 0:
            score_label = "(Bom)"
        elif predicted_value == 1:
            score_label = "(Ruim)"
        elif predicted_value == 2:
            score_label = "(Padrão)"
        else:
            score_label = str(predicted_value)

        st.markdown("Este cliente tem um Score de Crédito ** " + score_label + " **")
    else:
        st.markdown("Erro ao obter a previsão. Por favor, revise seus dados")

"""
## QuantumFinance - Predição de Score de Crédito 

Este modelo é capaz de prever um score de crédito ao cliente de acordo com o seu perfil.

A aplicação é para ser utilizada pelo time de backoffice da QuantumFinance,
por tal razão a avaliação se baseia no perfil e comportamento financeiro do cliente.

## Perfil do Cliente
Preencha os campos abaixo com as informações do cliente para obter a previsão do score de crédito.
"""
age = st.number_input(
    "Qual a idade do cliente?",step=1)

annual_income = st.number_input(
    "Qual a renda anual do cliente (em USD)?", step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver renda anual.")

monthly_inhand_salary = st.number_input(
    "Qual a renda mensal do cliente (em USD)?", step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver renda mensal.")

num_bank_accounts = st.number_input(
    "Quantas contas bancárias o cliente possui?",step=1, placeholder="Coloque 0, se nao houver contas bancárias.")

num_credit_card = st.number_input(
    "Quantos cartões de crédito o cliente possui?",step=1, placeholder="Coloque 0, se nao houver cartões de crédito.")

interest_rate = st.number_input(
    "Qual a taxa de juros dos cartões de crédito (em %)?",
    step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver cartões de crédito.")

num_of_loan = st.number_input(
    "Quantos empréstimos o cliente possui?",step=1, placeholder="Coloque 0, se nao houver empréstimos.")    

delay_from_due_date = st.number_input(
    "Qual o atraso em relação à data de vencimento (em dias)?",
    step=1, placeholder="Coloque 0, se nao houver atraso.")

num_of_delayed_payment = st.number_input(
    "Quantos pagamentos o cliente atrasou?",
    step=1, placeholder="Coloque 0, se nao houver atraso.")

changed_credit_limit = st.number_input(
    "Qual o limite de crédito alterado (em USD)?",
    step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver limite de crédito alterado.")

num_credit_inquiries = st.number_input(
    "Quantas consultas de crédito foram feitas?",
    step=1, placeholder="Coloque 0, se nao houver consultas de crédito.")

outstanding_debt = st.number_input(
    "Qual o tamanho da dívida em aberto (em USD)?", step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver dívida em aberto.")

total_emi_per_month = st.number_input(
    "Qual o valor total das parcelas mensais (em USD)?", step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver parcelas mensais.")

credit_utilization_ratio = st.number_input(
    "Qual a taxa de utilização de crédito (em %)?", step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver utilização de crédito.")

amount_invested_monthly = st.number_input(
    "Qual o valor investido mensalmente (em USD)?", step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver investimento mensal.")


monthly_balance = st.number_input(
    "Qual o saldo mensal (em USD)?", step=0.01, format="%.2f", placeholder="Coloque 0, se nao houver saldo mensal.")

credit_mix = st.selectbox(
    "Qual o mix de crédito do cliente?",
    options=["Padrão", "Ruim", "Bom", "Outro"],
    index=0
)

payment_behaviour = st.selectbox(
    "Qual o comportamento de pagamento do cliente?",
    options=["Gasta muito e faz pagamentos de alto valor",
             "Gasta muito e faz pagamentos de médio valor",
             "Gasta muito e faz pagamentos de baixo valor",
             "Gasta pouco e faz pagamentos de baixo valor",
             "Gasta pouco e faz pagamentos de médio valor",
             "Gasta pouco e faz pagamentos de alto valor",
             "Outro"],
    index=0
)

payment_of_min_amount = st.selectbox(
    "O cliente costuma fazer pagamentos de valor mínimo?",
    options=["Sim", "Não", "Outro"],
    index=0
)

if credit_mix == "Ruim":
    credit_mix = "bad"
elif credit_mix == "Bom":
    credit_mix = "good"
elif credit_mix == "Padrão":
    credit_mix = "standard"
elif credit_mix == "Outro":
    credit_mix = "other"
    
if payment_of_min_amount == "Sim":
    payment_of_min_amount = "yes"
elif payment_of_min_amount == "Não":
    payment_of_min_amount = "no"
elif payment_of_min_amount == "Outro":
    payment_of_min_amount = "other"

if payment_behaviour == "Gasta muito e faz pagamentos de alto valor":
    payment_behaviour = "high_spent_large_value_payments"
elif payment_behaviour == "Gasta muito e faz pagamentos de médio valor":
    payment_behaviour = "high_spent_medium_value_payments"
elif payment_behaviour == "Gasta muito e faz pagamentos de baixo valor":
    payment_behaviour = "high_spent_small_value_payments"
elif payment_behaviour == "Gasta pouco e faz pagamentos de baixo valor":
    payment_behaviour = "low_spent_small_value_payments"
elif payment_behaviour == "Gasta pouco e faz pagamentos de médio valor":
    payment_behaviour = "low_spent_medium_value_payments"
elif payment_behaviour == "Gasta pouco e faz pagamentos de alto valor":
    payment_behaviour = "low_spent_large_value_payments"
elif payment_behaviour == "Outro":
    payment_behaviour = "other"
    
#Prepara o payload para a request da API
payload = {
    "data": {
        "age": age,
        "annual_income": annual_income,
        "monthly_inhand_salary": monthly_inhand_salary,
        "num_bank_accounts": num_bank_accounts,
        "num_credit_card": num_credit_card,
        "interest_rate": interest_rate,
        "num_of_loan": num_of_loan,
        "delay_from_due_date": delay_from_due_date,
        "num_of_delayed_payment": num_of_delayed_payment,
        "changed_credit_limit": changed_credit_limit,
        "num_credit_inquiries": num_credit_inquiries,
        "credit_mix": credit_mix,
        "outstanding_debt": outstanding_debt,
        "credit_utilization_ratio": credit_utilization_ratio,
        "payment_of_min_amount": payment_of_min_amount,
        "total_emi_per_month": total_emi_per_month,
        "amount_invested_monthly": amount_invested_monthly,
        "payment_behaviour": payment_behaviour,
        "monthly_balance": monthly_balance
    }
}
      

if st.button("Calcular Score"):
    with st.spinner("Calculando..."):
        get_prediction(payload)