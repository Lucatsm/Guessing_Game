import streamlit as st
import requests
import uuid

# Configuração da página para usar o espaço total
st.set_page_config(page_title="Desafio da Palavra Misteriosa", layout="wide")

# URL do Webhook do n8n
WEBHOOK_URL = "https://lucatsm.app.n8n.cloud/webhook/desafio-palavra-misteriosa"

# 1. INICIALIZAÇÃO DOS ESTADOS DO JOGO (Session State)
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [{"role": "assistant", "content": "Olá! Escolha um gênero para começar e tente adivinhar a palavra misteriosa em 3 tentativas! Peça dicas!"}]
if "genero" not in st.session_state:
    st.session_state.genero = None
if "tentativas" not in st.session_state:
    st.session_state.tentativas = 3
if "palavra_oculta" not in st.session_state:
    # Começa com interrogações até a pessoa escolher um gênero
    st.session_state.palavra_oculta = "? ? ? ?"

# Título principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>DESAFIO DA PALAVRA MISTERIOSA</h1>", unsafe_allow_html=True)

# 2. LAYOUT EM DUAS COLUNAS
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("PASSO 1: ESCOLHA O GÊNERO")
    
    # Botões de Gênero
    c_acao, c_comedia, c_terror, c_drama = st.columns(4)
    if c_acao.button("🗡️\nAÇÃO"):
        st.session_state.genero = "Ação"
        st.session_state.palavra_oculta = "_ _ _ _ _ _ _ _" # 8 letras
        st.session_state.mensagens.append({"role": "assistant", "content": "Gênero AÇÃO selecionado. A palavra tem 8 letras. Qual é a sua primeira pergunta ou chute?"})
        
    if c_comedia.button("😂\nCOMÉDIA"):
        st.session_state.genero = "Comédia"
        st.session_state.palavra_oculta = "_ _ _ _ _ _" # 6 letras
        st.session_state.mensagens.append({"role": "assistant", "content": "Gênero COMÉDIA selecionado. A palavra tem 6 letras. Qual é a sua primeira pergunta ou chute?"})
        
    if c_terror.button("👻\nTERROR"):
        st.session_state.genero = "Terror"
        st.session_state.palavra_oculta = "_ _ _ _ _ _ _ _ _" # 9 letras
        st.session_state.mensagens.append({"role": "assistant", "content": "Gênero TERROR selecionado. A palavra tem 9 letras. Qual é a sua primeira pergunta ou chute?"})
        
    if c_drama.button("🎭\nDRAMA"):
        st.session_state.genero = "Drama"
        st.session_state.palavra_oculta = "_ _ _ _ _" # 5 letras
        st.session_state.mensagens.append({"role": "assistant", "content": "Gênero DRAMA selecionado. A palavra tem 5 letras. Qual é a sua primeira pergunta ou chute?"})
        
    st.markdown("---")
    
    # Área da Palavra Oculta e Tentativas
    st.subheader("A PALAVRA OCULTA:")
    st.markdown(f"<h2 style='letter-spacing: 5px;'>{st.session_state.palavra_oculta}</h2>", unsafe_allow_html=True)
    
    st.metric(label="TENTATIVAS RESTANTES:", value=st.session_state.tentativas)

with col2:
    st.subheader("🤖 CONVERSE COM A LMM (DICAS E ADIVINHAÇÃO)")
    
    # Container do Chat
    container_chat = st.container(height=400)
    
    # Exibir histórico de mensagens
    with container_chat:
        for msg in st.session_state.mensagens:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    
    # 3. ENTRADA DO USUÁRIO E COMUNICAÇÃO COM A API
    if prompt := st.chat_input("Digite sua pergunta ou palpite..."):
        # Adiciona a mensagem do jogador na tela
        st.session_state.mensagens.append({"role": "user", "content": prompt})
        with container_chat:
            with st.chat_message("user"):
                st.markdown(prompt)
        
        # Preparar os dados para o n8n
        payload = {
            "message": prompt,
            "sessionId": st.session_state.session_id
        }
        
        # Enviar o POST para a API e exibir indicador de carregamento
        try:
            with st.spinner("A LMM está pensando..."):
                resposta_api = requests.post(WEBHOOK_URL, json=payload)
                
                if resposta_api.status_code == 200:
                    # Lê o JSON retornado pelo n8n
                    dados_json = resposta_api.json()
                    
                    # Pega a chave 'resposta'
                    texto_resposta = dados_json.get("resposta", "A IA não enviou uma resposta.")
                else:
                    texto_resposta = f"Erro na conexão com a API. Status: {resposta_api.status_code}"
                    
        except Exception as e:
            texto_resposta = f"Erro ao conectar com o webhook: {e}"
            
        # Adiciona a resposta da IA na tela
        st.session_state.mensagens.append({"role": "assistant", "content": texto_resposta})
        st.rerun()