from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *
import json
from tools_ecomart import *


load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4o"
#contexto = carrega("./dados/ecomart.txt")

def pegar_json():
    filename = "./assistentes.json"
    
    if not os.path.exists(filename):
        assistant_id = criar_assistente()
        file_id_list = criar_lista_ids()

        # Atualiza o assistente com vetor de arquivos
        assistant = cliente.beta.assistants.update(
            assistant_id = assistant_id.id,
            tool_resources = {"file_search":
                                {"vector_store_ids": [file_id_list.id]}
                            },
        )

        thread_id = criar_thread()
        
        data = {
            "assistant_id": assistant.id,
            "thread_id": thread_id.id,
            "file_ids": file_id_list.id
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Arquivo 'assistentes.json' criado com sucesso.")
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Arquivo 'assistentes.json' não encontrado.")


def criar_assistente():
    assistente = cliente.beta.assistants.create(
        name="Atendente EcoMart2",
        instructions = f"""
                Você é um chatbot de atendimento a clientes de um e-commerce. 
                Você não deve responder perguntas que não sejam dados do ecommerce informado!
                Além disso, acesse os arquivos associados a você e a thread para responder as perguntas.
                """,
        model = modelo,
        #tools=[{"type": "file_search"}]
        tools = minhas_tools
    )
    return assistente

def criar_lista_ids():

    # Create a vector store caled "Financial Statements"
    vector_store = cliente.beta.vector_stores.create(name="Docs Ecomart")
    
    # Ready the files for upload to OpenAI
    file_paths = ["./dados/dados_ecomart.txt",
                  "./dados/políticas_ecomart.txt",
                  "./dados/produtos_ecomart.txt"]
    file_streams = [open(path, "rb") for path in file_paths]
    
    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    file_batch = cliente.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id = vector_store.id,
        files = file_streams
    )
    
    # You can print the status and the file counts of the batch to see the result of this operation.
    print(file_batch.status)
    print(file_batch.file_counts)

    return vector_store

def criar_thread():
    return cliente.beta.threads.create()
