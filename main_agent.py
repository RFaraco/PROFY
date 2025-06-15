import streamlit as st
import requests

st.title("🤖 Assistente Educacional - Biologia 101")

# Prompt do professor
prompt_do_professor = """
Você é um assistente virtual da disciplina de Introdução à Biologia.
Seu objetivo é ajudar os alunos a compreenderem os conceitos explicando de forma clara e objetiva.
Seja gentil, paciente e incentive o aluno a refletir.
Não responda perguntas que não tenham relação com o conteúdo da disciplina.
"""

# Entrada do aluno
pergunta = st.text_input("Digite sua pergunta aqui:")

# Seu token Hugging Face
api_token = st.secrets["HUGGINGFACE_API_TOKEN"]

def responder(pergunta):
    entrada = f"{prompt_do_professor}\n\nPergunta do aluno: {pergunta}\n\nResposta:"
    
    response = requests.post(
        "https://api-inference.huggingface.co/models/google/flan-t5-base",
        headers={"Authorization": f"Bearer {api_token}"},
        json={"inputs": entrada}
    )

    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"].split("Resposta:")[-1].strip()
    else:
        return "⚠️ Erro ao gerar resposta. Verifique a API ou tente novamente."

# Mostra resposta
if st.button("Perguntar"):
    if pergunta.strip():
        with st.spinner("Consultando o assistente..."):
            resposta = responder(pergunta)
            st.markdown(f"**Resposta:** {resposta}")
    else:
        st.warning("Digite uma pergunta válida.")
