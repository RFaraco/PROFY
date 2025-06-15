import streamlit as st
import requests

# Interface
st.title("Assistente Virtual do Curso")

# Simula prompt vindo do professor
prompt_do_professor = """Você é um assistente de ensino da disciplina de Introdução à Biologia. Seja amigável, explique conceitos com clareza e só responda com base em fontes confiáveis."""

# Entrada do aluno
pergunta = st.text_input("Digite sua pergunta aqui:")

# Botão de envio
if st.button("Perguntar"):
    with st.spinner("Gerando resposta..."):

        # Monta a entrada para o modelo
        entrada = f"{prompt_do_professor}\n\nPergunta do aluno: {pergunta}\n\nResposta:"

        # Chamada ao modelo gratuito (Hugging Face)
        resposta = requests.post(
            "https://api-inference.huggingface.co/models/microsoft/Phi-2",
            headers={"Authorization": "Bearer SUA_API_HUGGINGFACE"},
            json={"inputs": entrada}
        )

        if resposta.status_code == 200:
            texto_gerado = resposta.json()[0]['generated_text']
            st.write(texto_gerado.split("Resposta:")[-1])
        else:
            st.error("Erro ao gerar resposta. Verifique a API ou tente novamente.")
