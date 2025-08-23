import os

from langchain.chat_models import init_chat_model
from project.scrapping import retorna_dicinario
from embedding import criar_vector_store

# Carrega API Keys do ambiente
langsmith_key = os.getenv("LANGSMITH_API_KEY")
user_agent = os.getenv("USER_AGENT", "lia-project")

result = retorna_dicinario()
vector_store = criar_vector_store(result)

# Inicializa LLM NVIDIA
llm = init_chat_model(
    "nvidia/llama-3.1-nemotron-70b-instruct",
    model_provider="nvidia"
)

def retrieve(question):
    return vector_store.similarity_search(question)

def generate(question):
    retrieved_docs = retrieve(question)
    context_text = "\n\n".join(
        [f"Número: {doc.metadata['numero']}\nRamo: {doc.metadata['ramo']}\nTexto: {doc.page_content}"
         for doc in retrieved_docs]
    )
    #print("context_text = ", context_text) #
    messages = (f"Dado o excerto retorne o número da súmula o ramo e a súmula no qual ele se enquadra. Diga somente"
                f" isso, caso o excerto não se enquadrar no contexto fornecido responda <Não se enquadra em nenhuma das 676 súmulas do STJ>"
                f"Não faça comentarios nem sinteses desnecessarias. Excerto = {question}\n Súmulas: \n{context_text}")
    print(context_text)
    response = llm.invoke(messages)
    return response.content #resposta da llm

arquivo = input("Digite o nome do arquivo com os excertos: ").strip()

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()  # lê o arquivo inteiro
        blocos = [bloco.strip() for bloco in conteudo.split("\n\n") if bloco.strip()] # blocos separados por uma linha em branco
except FileNotFoundError:
    print(f"Arquivo '{arquivo}' não encontrado.")
    exit()

# Processa cada excerto
for excerto in blocos:
    resposta = generate(excerto)
    print("Excerto:", excerto)
    print("Resposta:", resposta)
    print("-" * 75)