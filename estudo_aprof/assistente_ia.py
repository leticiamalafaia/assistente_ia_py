#Estudo de caso 1 - DSA AI Coder - Criando Seu Assistente de Programação, em Python

# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar á API da plataforma Groq e acessa o LLM

from groq import Groq

#Configura as página do Streamlit com titulo ícone, layout e estudo inicial da sidebar

st.set_page_config(
    page_title = "DSA IA Code",
    page_icon= "🤖",
    layout = "wide",
    initial_sidebar_state="expanded"
)

#Define um prompt de sistema que descreve as regras e comportamento de asstitente de IA

CUSTOM_PROMPT ="""
Você é o "DSA Coder", um assistente de IA especialista em programação, com foco principal em Python. Sua missão é ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivamente em auxiliar com código.
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteúdo da barra lateral no Streamlit

with st.sidebar:

    #Define o titulo da barra lateral
    st.markdown("Um assistente de IA focada em programação Python para ajudar iniciantes.")

    # Mostra um texto explicativo sobre o assistente 
    st.markdown("Um assistente de IA focado em programação Python para ajudar iniciantes.")

    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obitenha sua chave em https://console.groq.com/keys"
    )

    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Python. IA pode cometer erros. Sempre verifique as respostas.")

    st.markdown("---")
    st.markdown("Conheça os Cursos Individuais, Formações e Programas de Pós-Graduação da DSA:")

    #Link para o site da DSA 
    st.markdown("🔗 [Data Science Academy](https://www.datascienceacademy.com.br)")

#Título princial do app
st.title("Data Science Academy - DSA IA Coder")

#Subtítulo adicional
st.title("Assistente Pessoal de Programação Pyton 🐍")

#texto auxiliar abaixo do título
st.caption("Faça sua pergunta sobre a Linguagem Python e obtenha código, explicações e referências.")

#Inicializa o historico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Inicializa a variavel do cliente Groq como None
client = None

# Verifica se o usuário a chave da API do Groq

if groq_api_key:

    try:

        #Cria cliente Groq com a chave de API fornecidas
        client = Groq(api_key = groq_api_key)
    except Exception as e:

        #Exibe erro caso haja problema ao inicializr o cliente
        st.sidebar.error(f"Erro ao incializar o cliente Groq: {e}")
        st.stop()

#Caso não tenha chave, mas já existam mensagens, mostra aviso
elif st.session_state.messages:
    st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

#Captura a entrada do usuário no chat
if prompt := st.chat_input("Qual sua dúvida sobre Python?"):

    #Se não ouver cliente válido, mostra aviso e para a execução 
    if not client: 
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar.")
        st.stop()

        # Armazena a mesnagem do usuário no estado da sessão
    st.session_state.messages.appende({"role":"user", "content": prompt})

        #Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
            st.markdown(prompt)

    #Prepara a mensagens para enviar á API, ibcluindo prompt de sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:

        messages_for_api.append(msg)

    #Cria a resposta do assistente no chat
    with st.chat_message("assistant"):

        with st.spinner("Analisando sua pergunta... "):

            try:

                ## Chama a API da Groq para gerar a resposta do assistente
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b", 
                    temperature = 0.7,
                    max_tokens = 2048,
                )

                # Extrai a resposta gerada pela API
                dsa_ia_resposta = chat_completion.choices[0].message.content

                # Exibe a resposta do Streamlit
                st.markdown(dsa_ia_resposta)

                #Armazena respostas do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": dsa_ia_resposta})

            #Caso ocorra erro na comunicação  com a API, exibe mensagem de erro
            except Exception as e:
                st.error(f"Ocorre um erro ao se comunicar com API da Groq: {e}")

st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p>DSA AI Coder - Parte Integrante do Curso Gratuito Fundamentos de Linguagem Python da Data Science Academy</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Obrigado DSA