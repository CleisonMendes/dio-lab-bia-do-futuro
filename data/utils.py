import json
import pandas as pd
import os
import streamlit as st
import google.generativeai as genai

# ************ CONFIGURAÇÃO GEMINI ************
# Sua chave de API
GOOGLE_API_KEY = "SUA_CHAVE_API_AQUI" 
genai.configure(api_key=GOOGLE_API_KEY)

# --- PROTEÇÃO CONTRA ERRO 404 ---
# Esta função encontra automaticamente um modelo que funcione na sua conta
def encontrar_modelo_disponivel():
    try:
        print(">>> Buscando modelos disponíveis na sua conta...")
        for m in genai.list_models():
            # Procura por modelos que geram texto (Flash ou Pro)
            if 'generateContent' in m.supported_generation_methods:
                if 'flash' in m.name: # Prioridade para o Flash (mais rápido)
                    print(f">>> Modelo encontrado e selecionado: {m.name}")
                    return m.name
        # Se não achar Flash, usa o padrãozão Gemini Pro
        return "models/gemini-pro"
    except Exception as e:
        print(f"Erro ao listar modelos: {e}")
        return "models/gemini-pro" # Fallback de segurança

# Define o modelo automaticamente sem dar erro 404
MODELO_ESCOLHIDO = encontrar_modelo_disponivel()
model = genai.GenerativeModel(MODELO_ESCOLHIDO)

# ************ CONFIGURAÇÃO DE PASTAS ************
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')

# ************ CARREGAR DADOS ************
try:
    perfil = json.load(open(os.path.join(DATA_DIR, 'perfil_investidor.json'), 'r', encoding='utf-8'))
    produtos = json.load(open(os.path.join(DATA_DIR, 'produtos_financeiros.json'), 'r', encoding='utf-8'))
    transacoes = pd.read_csv(os.path.join(DATA_DIR, 'transacoes.csv'), encoding='utf-8')
    historico = pd.read_csv(os.path.join(DATA_DIR, 'historico_atendimento.csv'), encoding='utf-8')
except Exception as e:
    st.error(f"Erro crítico ao carregar arquivos: {e}")
    st.stop()

# ************ CONTEXTO E PROMPT ************
contexto = f"""
PERFIL DO CLIENTE:
Nome: {perfil['nome']} | Idade: {perfil['idade']}
Perfil: {perfil['perfil_investidor']} | Objetivo: {perfil['objetivo_principal']}
Patrimônio: R$ {perfil['patrimonio_total']} | Reserva: R$ {perfil['reserva_emergencia_atual']}

HISTÓRICO RECENTE:
{transacoes.tail(5).to_string(index=False)}

PRODUTOS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = """PERSONA: Sophia, educadora financeira objetiva.
OBJETIVO: Tirar dúvidas em APENAS 1 PARÁGRAFO CURTO (estilo mensagem de WhatsApp).

REGRAS RÍGIDAS:
1. MÁXIMO DE 50 PALAVRAS. Seja extremamente concisa.
2. Use o saldo do cliente para exemplificar.
3. Sem introduções como "Olá", "Claro", "Entendi". Vá direto à resposta.
4. Se perguntarem "O que é", dê a definição e um exemplo com o dinheiro dele. Fim.
"""

# ************ FUNÇÃO DE PERGUNTA ************
def perguntar(msg):
    prompt_final = f"{SYSTEM_PROMPT}\n\nDADOS DO CLIENTE:\n{contexto}\n\nPERGUNTA: {msg}"
    try:
        response = model.generate_content(prompt_final)
        return response.text if response.text else "Erro: Resposta vazia."
    except Exception as e:
        return f"Erro na conexão ({MODELO_ESCOLHIDO}): {e}"

# ============ INTERFACE ============
st.set_page_config(page_title="Sophia Finanças", page_icon="💰")
st.title("🎓 Sophia, Sua Educadora Financeira")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if pergunta := st.chat_input("Dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    st.session_state.messages.append({"role": "user", "content": pergunta})

    with st.spinner(f"Sophia pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})