from flask import Flask,render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_documento import *
from selecionar_persona import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4o"

minhas_tools = [
    #{"type":    "retrieval"},
    {"type":    "file_search"},
    {"type":    "function",
                "function": {
                    "name": "validar_codigo_promocional",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        "codigo": {
                            "type": "string",
                            "description": "O código promocional, no formato, CUPOM_XX. Por exemplo: CUPOM_ECO"
                        },
                        "validade": {
                            "type": "string",
                            "description": "A validade do cupom, caso seja válido e esteja associado as políticas. No formato DD/MM/YYYY."
                        }
                        },
                        "required": ["codigo","validade"]
                    },
                    "description": "Valide um código promocional com base nas diretrizes de Descontos e Promoções da empresa"
                }
    }
    
]

def validar_codigo_promocional(argumentos):
    codigo = argumentos.get("codigo")
    validade = argumentos.get("validade")

    return f"""
        
        # Formato de Resposta
        
        {codigo} com validade: {validade}. 
        Ainda, diga se é válido ou não para o usuário.
        Sempre informe um produto disponível da Ecomart caso o cupom seja válido.
        Se o cupom não for válido ou não existir, indique um cupom existente nas Políticas do EcoMart.

        """

minhas_funcoes = {
    "validar_codigo_promocional": validar_codigo_promocional,
}