# 🎮 Desafio da Palavra Misteriosa

Jogo de adivinhação interativo que combina mecânica clássica de palavras com conversa livre com uma Inteligência Artificial.

O jogador escolhe um gênero (Ação, Comédia, Terror ou Drama) e tenta descobrir uma palavra secreta relacionada a ele. Ele tem apenas **3 tentativas oficiais**. Entre os chutes, pode conversar livremente com a LLM para pedir dicas, fazer perguntas ou tentar “convencer” a IA a revelar informações.

A IA conhece a palavra secreta, mas segue regras rígidas para não entregar a resposta de forma direta.

---

## ✨ Funcionalidades

- Escolha de 4 gêneros (Ação, Comédia, Terror e Drama)
- Geração de palavra secreta relacionada ao gênero
- Chat livre com a LLM (dicas, perguntas, negociação)
- Sistema de 3 tentativas oficiais
- Interface visual com palavra oculta e contador de tentativas
- System prompt com guardrails para controlar o comportamento da IA

---

## 🛠️ Tecnologias

- **Frontend:** Streamlit/Gradio
- **Backend:** Python (FastAPI) ou Node.js
- **LLM:** Google Gemini API (tier gratuito)

---

## 🧠 Como a IA funciona
A LLM recebe um System Prompt rigoroso que define:

A palavra secreta atual
O gênero escolhido
Quantas tentativas restam
Regras claras de não revelar a resposta
Tom de resposta de acordo com o gênero

O backend controla o estado da partida (palavra secreta, tentativas restantes e histórico de mensagens) e só envia para o frontend as informações necessárias.

---

## 👥 Integrantes

Luca Tiepolo Schmidt Morete — RM 560255
Carlos Bucker — RM 555812

---

## 📄 Licença
Este projeto foi desenvolvido como atividade acadêmica da Faculdade FIAP.

Sinta-se livre para usar e adaptar para fins educacionais

---
